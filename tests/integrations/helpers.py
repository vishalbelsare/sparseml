# Copyright (c) 2021 - present / Neuralmagic, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import os

import pytest
import yaml


def get_configs_with_cadence(cadence: str, dir_path: str = "."):
    all_files_found = glob.glob("test*.test", root_dir=dir_path)
    matching_files = []
    for file in all_files_found:
        config = yaml.safe_load(file)
        if config.get("cadence") == cadence:
            matching_files.append(config)
        # read one line a time