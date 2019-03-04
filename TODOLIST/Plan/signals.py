import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import Plantodo


@receiver(post_save, sender=Plantodo)
def log_TODOLIST_updated_added_event(sender, **kwargs):
	"""Writes information about newly added or updated plan into log file"""
	logger = logging.getLogger(__name__)

	plan = kwargs['instance']
	if kwargs['created']:
		logger.info("Plan added: %s (ID: %s)" % (plan.title, plan.id))
	else:
		logger.info("Plan updated: %s (ID: %s)" % (plan.title, plan.id))

@receiver(post_delete, sender=Plantodo)
def log_TODOLIST_deleted_event(sender, **kwargs):
	"""Writes information about newly deleted plan into log file"""
	logger = logging.getLogger(__name__)

	plan = kwargs['instance']
	logger.info("Plan deleted: %s (ID: %s)" % (plan.title, plan.id))
	