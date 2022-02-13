from apps.integrations.mock_lib.model import User
from apps.integrations.mock_lib.mock import MockLib
from apps.integrations.mock_lib.mock import Status
import logging

logger = logging.getLogger(__name__)

def update_user_external_system(user):
    # Convert user into mock_lib User model
    external_user = User(user.integration_id, user.name, user.email)
    # Call external lib update
    status = MockLib.update_user(external_user)
    userId = str(user.id)
    # If it fails, just log the error and carry on with the execution
    if status == Status.FAIL:
        logger.error('External system failed to update user ' + userId)
    else:
        logger.info('User ' + userId + ' updated on external system')
