from celery.utils.log import get_task_logger
from .email import send_trip_email
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task(name='send_email_task')
def send_email_task(name, email, coordinates, distance):
    logger.info('Sent email')
    return send_trip_email(name, email, coordinates, distance)
