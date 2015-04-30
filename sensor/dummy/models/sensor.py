#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


from sensor.core.models import Sensor
from sensor.dummy.forms import DummyEventUploadForm


class DummySensor(Sensor):

    @classmethod
    def event_upload_form(cls):
        return DummyEventUploadForm

    @classmethod
    def sensor_type_name(self):
        return "dummy_sensor"