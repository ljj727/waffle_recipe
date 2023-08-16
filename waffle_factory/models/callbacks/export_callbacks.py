import sys
from collections import defaultdict
from copy import deepcopy
import wandb as wb

# Exporter callbacks ---------------------------------------------------------------------------------------------------
def on_export_start(exporter):
    wb.run.name = f"{sys.argv[1]}-{exporter.args.mode}-{exporter.args.format}"
    wb.config.update(vars(exporter.args))
    wb.run.tags = ["YOLOv8"] + [exporter.args.task] + [exporter.args.mode] + [exporter.args.format] + [sys.argv[1]]
    wb.run.save()

def on_export_end(exporter):
    art = wb.Artifact(type='model', name=f'run_{wb.run.id}_model')
    art.add_file(f"{exporter.file.parent}/best.{exporter.args.format}")
    wb.run.log_artifact(art, aliases=[exporter.args.format])


default_callbacks = {
    # Run in exporter
    'on_export_start': [on_export_start],
    'on_export_end': [on_export_end]}

def export_callbacks():
    return defaultdict(list, deepcopy(default_callbacks))