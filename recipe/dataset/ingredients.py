import git

from pathlib import Path
from typing import Union
from dvc.api import DVCFileSystem
from dvc.repo import Repo
from waffle_hub.dataset import Dataset
from recipe.configs import dvc_settings

from github import Github


class Ingredients:
    """Waffle Recipe Ingredients

    Attributes:
        repo (str): Repository path
         (str): 
    """

    def __init__(
        self,
        repo: Union[str, Path],
        url: str = None,
    ):
        self.repo = Path(repo)
        if url is None:
            self.git_repo = git.Repo(repo)
        elif url.endswith('.git'):
            self.git_repo = git.Repo.clone_from(url, repo)
        else:
            raise ValueError("Invalid URL")

        self.dvc_repo = Repo(repo)
        self.dvc = DVCFileSystem(
            repo=self.dvc_repo
        )
    
    def __repr__(self):
        return f"Ingredients(repo={self.repo})"

    @classmethod
    def init(cls, path=None): # Config를 통해서 진행할 수 있게 하자.
        # if dvc_settings.default_config:
        #     print("Please enter Git information in the .env file.")

        g = Github(dvc_settings.GITHUB_SECRET_ACCESS_KEY)
        user = g.get_user()
        print(f"Logged in as: {user.login}")

        if path is None:
            path = './data'
        repo = git.Repo.clone_from(dvc_settings.GITHUB_URL, path)
        for remote in repo.remotes:
            remote.fetch()
        for ref in repo.refs: 
            print(ref.name)
        for remote_branch in repo.remote().refs:
            local_branch_name = remote_branch.remote_head
            repo.create_head(local_branch_name, remote_branch).set_tracking_branch(remote_branch)

    def download(self): # Data Download
        self.dvc.repo.pull()

    def upload(self): # Data Upload
        self.dvc.repo.add("data")
        self.dvc.repo.push()

    def info(self):
        status = self.dvc.repo.status()
        print(status)
        return status

    def waffle_info(self):

        dataset = Dataset.load(
            name='PeopleDataset_Iwest_v1.1.0c', 
            root_dir= '/home/ljj/ws/dvc_test/data'
        )
        per_category = dataset.get_num_images_per_category()
        categories = dataset.get_categories()
        num_images = len(dataset.get_images())

    def list(self): # Data List Logging

        for remote in self.git_repo.remotes:
            remote.fetch()
        branches = self.git_repo.branches
        print("브랜치 리스트:")
        for branch in branches:
            print(branch.name)

        for branch in branches:
            print(f"\n브랜치: {branch.name}")
            self.git_repo.git.checkout(branch.name)
            commits = list(self.git_repo.iter_commits(branch.name))
            branch_tags = []
            for tag in self.git_repo.tags:
                if tag.commit in commits:
                    branch_tags.append(tag)
                    
            if branch_tags:
                print("이 브랜치에 해당하는 태그:")
                for tag in branch_tags:
                    tag_name = tag.name
                    tag_commit = tag.commit.hexsha
                    tag_message = tag.tag.message if tag.tag else "태그 메시지가 없습니다"
                    
                    print(f"태그 이름: {tag_name}")
                    print(f"커밋 해시: {tag_commit}")
                    print(f"태그 메시지: {tag_message}")
                    print('-' * 40)
            else:
                print("이 브랜치에 해당하는 태그가 없습니다.")

    def select(self, tag_name: str): # Data Select
        self.git_repo.git.checkout(tag_name)
        print(f'태그 {tag_name}로 체크아웃 완료')
    
    def create(self, tag_name: str, message: str): # Data Change & Update
        self.git_repo.create_tag(tag_name, message)
        print(f'태그 {tag_name} 생성 완료')
    
    def reproduce(self): # 뭔가 불편한데...
        self.dvc.repo.reproduce(str(self.repo / 'dvc.yaml'))
    
        
        





    