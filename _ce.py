# this file is only used for continuous evaluation test!

import os
import sys
sys.path.append(os.environ['ceroot'])
from kpi import CostKpi
from kpi import DurationKpi
from kpi import AccKpi


each_pass_duration_cpu1_thread1_kpi = DurationKpi('each_pass_duration_cpu1_thread1', 0.08, 0, actived=True)
train_loss_cpu1_thread1_kpi = CostKpi('train_loss_cpu1_thread1', 0.08, 0)
train_auc_val_cpu1_thread1_kpi = AccKpi('train_auc_val_cpu1_thread1', 0.08, 0)
train_batch_auc_val_cpu1_thread1_kpi = AccKpi('train_batch_auc_val_cpu1_thread1', 0.08, 0)
each_pass_duration_cpu1_thread8_kpi = DurationKpi('each_pass_duration_cpu1_thread8', 0.08, 0, actived=True)
train_loss_cpu1_thread8_kpi = CostKpi('train_loss_cpu1_thread8', 0.08, 0)
train_auc_val_cpu1_thread8_kpi = AccKpi('train_auc_val_cpu1_thread8', 0.08, 0)
train_batch_auc_val_cpu1_thread8_kpi = AccKpi('train_batch_auc_val_cpu1_thread8', 0.08, 0)
each_pass_duration_cpu8_thread8_kpi = DurationKpi('each_pass_duration_cpu8_thread8', 0.08, 0, actived=True)
train_loss_cpu8_thread8_kpi = CostKpi('train_loss_cpu8_thread8', 0.08, 0)
train_auc_val_cpu8_thread8_kpi = AccKpi('train_auc_val_cpu8_thread8', 0.08, 0)
train_batch_auc_val_cpu8_thread8_kpi = AccKpi('train_batch_auc_val_cpu8_thread8', 0.08, 0)

tracking_kpis = [
        each_pass_duration_cpu1_thread1_kpi,
        train_loss_cpu1_thread1_kpi,
        train_auc_val_cpu1_thread1_kpi,
        train_batch_auc_val_cpu1_thread1_kpi,
        each_pass_duration_cpu1_thread8_kpi,
        train_loss_cpu1_thread8_kpi,
        train_auc_val_cpu1_thread8_kpi,
        train_batch_auc_val_cpu1_thread8_kpi,
        each_pass_duration_cpu8_thread8_kpi,
        train_loss_cpu8_thread8_kpi,
        train_auc_val_cpu8_thread8_kpi,
        train_batch_auc_val_cpu8_thread8_kpi,
        ]


def parse_log(log):
    '''
    This method should be implemented by model developers.
    The suggestion:
    each line in the log should be key, value, for example:
    "
    train_cost\t1.0
    test_cost\t1.0
    train_cost\t1.0
    train_cost\t1.0
    train_acc\t1.2
    "
    '''
    for line in log.split('\n'):
        fs = line.strip().split('\t')
        print(fs)
        if len(fs) == 3 and fs[0] == 'kpis':
            kpi_name = fs[1]
            kpi_value = float(fs[2])
            yield kpi_name, kpi_value


def log_to_ce(log):
    kpi_tracker = {}
    for kpi in tracking_kpis:
        kpi_tracker[kpi.name] = kpi

    for (kpi_name, kpi_value) in parse_log(log):
        print(kpi_name, kpi_value)
        kpi_tracker[kpi_name].add_record(kpi_value)
        kpi_tracker[kpi_name].persist()


if __name__ == '__main__':
    log = sys.stdin.read()
    log_to_ce(log)
