# Copyright 2024 The KerasNLP Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest

from keras_nlp.src.models.backbone import Backbone
from keras_nlp.src.models.bert.bert_backbone import BertBackbone
from keras_nlp.src.models.bert.bert_text_classifier import BertTextClassifier
from keras_nlp.src.models.text_classifier import TextClassifier
from keras_nlp.src.tests.test_case import TestCase


class TestTask(TestCase):
    @pytest.mark.large
    def test_convert_tiny_preset(self):
        model = BertTextClassifier.from_preset(
            "hf://google-bert/bert-base-uncased", num_classes=2
        )
        prompt = "That movies was terrible."
        model.predict([prompt])

    @pytest.mark.large
    def test_class_detection(self):
        model = TextClassifier.from_preset(
            "hf://google-bert/bert-base-uncased",
            num_classes=2,
            load_weights=False,
        )
        self.assertIsInstance(model, BertTextClassifier)
        model = Backbone.from_preset(
            "hf://google-bert/bert-base-uncased",
            load_weights=False,
        )
        self.assertIsInstance(model, BertBackbone)

    # TODO: compare numerics with huggingface model