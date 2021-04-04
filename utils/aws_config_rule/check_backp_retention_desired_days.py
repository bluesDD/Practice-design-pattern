from rdklib import Evaluator, Evaluation, ConfigRule, ComplianceType


APPLICABLE_RESOURCES = ["AWS::Backup::Plan"]


class Backup_RETENTION_DAYS(ConfigRule):

  def evaluate_backup_rule(self, event, client_factory, confguration_item, valid_rule_parameters):
    backup_client = client_factory.build_client('backup')
    

