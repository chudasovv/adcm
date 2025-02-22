# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cm.logger import logger
from cm.errors import AdcmEx

from cm.models import Prototype, Action


def task_generator(action, selector):
    logger.debug("call task_generator: %s", action)
    try:
        service = Prototype.objects.get(type='service', name='ZOOKEEPER', version='1.2')
    except Prototype.DoesNotExist:
        raise AdcmEx('TASK_GENERATOR_ERROR', 'service ZOOKEEPER not found') from None

    try:
        stop = Action.objects.get(context='service', context_id=service.id, name='stop')
    except Prototype.DoesNotExist:
        raise AdcmEx('TASK_GENERATOR_ERROR', 'action stop of service ZOOKEEPER not found') from None

    try:
        start = Action.objects.get(context='service', context_id=service.id, name='start')
    except Prototype.DoesNotExist:
        raise AdcmEx('TASK_GENERATOR_ERROR', 'action start of service ZOOKEEPER not found') from None

    return (
        {'action': stop, 'selector': selector},
        {'action': start, 'selector': selector},
    )


def task_get(action, selector):
    logger.debug("call task: %s", action)
    try:
        service = Prototype.objects.get(type='service', name='Simple_service')
    except Prototype.DoesNotExist:
        raise AdcmEx('TASK_GET_ERR', 'my error description') from None
    try:
        stop = Action.object.get(context='service', context_id=service.id, name='stop')
    except Prototype.DoesNotExist:
        raise AdcmEx('TASK_GENERATOR_ERROR', 'action stop in service Simple_service not found') from None

    return {'action': stop, 'selector': selector}
