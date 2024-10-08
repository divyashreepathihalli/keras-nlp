"""Tests for iou functions."""

import numpy as np

from keras_hub.src.bounding_box import iou as iou_lib
from keras_hub.src.tests.test_case import TestCase


class IoUTest(TestCase):
    def test_compute_single_iou(self):
        bb1 = np.array([[100, 101, 200, 201]])
        bb1_off_by_1 = np.array([[101, 102, 201, 202]])
        # area of bb1 and bb1_off_by_1 are each 10000.
        # intersection area is 99*99=9801
        # iou=9801/(2*10000 - 9801)=0.96097656633
        self.assertAllClose(
            iou_lib.compute_iou(bb1, bb1_off_by_1, "yxyx")[0], [0.96097656633]
        )

    def test_compute_iou(self):
        bb1 = [100, 101, 200, 201]
        bb1_off_by_1_pred = [101, 102, 201, 202]
        iou_bb1_bb1_off = 0.96097656633
        top_left_bounding_box = [0, 2, 1, 3]
        far_away_box = [1300, 1400, 1500, 1401]
        another_far_away_pred = [1000, 1400, 1200, 1401]

        # Rows represent predictions, columns ground truths
        expected_result = np.array(
            [[iou_bb1_bb1_off, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]],
            dtype=np.float32,
        )

        sample_y_true = np.array([bb1, top_left_bounding_box, far_away_box])
        sample_y_pred = np.array(
            [bb1_off_by_1_pred, top_left_bounding_box, another_far_away_pred],
        )

        result = iou_lib.compute_iou(sample_y_true, sample_y_pred, "yxyx")
        self.assertAllClose(expected_result, result)

    def test_batched_compute_iou(self):
        bb1 = [100, 101, 200, 201]
        bb1_off_by_1_pred = [101, 102, 201, 202]
        iou_bb1_bb1_off = 0.96097656633
        top_left_bounding_box = [0, 2, 1, 3]
        far_away_box = [1300, 1400, 1500, 1401]
        another_far_away_pred = [1000, 1400, 1200, 1401]

        # Rows represent predictions, columns ground truths
        expected_result = np.array(
            [
                [[iou_bb1_bb1_off, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]],
                [[iou_bb1_bb1_off, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]],
            ],
        )

        sample_y_true = np.array(
            [
                [bb1, top_left_bounding_box, far_away_box],
                [bb1, top_left_bounding_box, far_away_box],
            ],
        )
        sample_y_pred = np.array(
            [
                [
                    bb1_off_by_1_pred,
                    top_left_bounding_box,
                    another_far_away_pred,
                ],
                [
                    bb1_off_by_1_pred,
                    top_left_bounding_box,
                    another_far_away_pred,
                ],
            ],
        )

        result = iou_lib.compute_iou(sample_y_true, sample_y_pred, "yxyx")
        self.assertAllClose(expected_result, result)

    def test_batched_boxes1_unbatched_boxes2(self):
        bb1 = [100, 101, 200, 201]
        bb1_off_by_1_pred = [101, 102, 201, 202]
        iou_bb1_bb1_off = 0.96097656633
        top_left_bounding_box = [0, 2, 1, 3]
        far_away_box = [1300, 1400, 1500, 1401]
        another_far_away_pred = [1000, 1400, 1200, 1401]

        # Rows represent predictions, columns ground truths
        expected_result = np.array(
            [
                [[iou_bb1_bb1_off, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]],
                [[iou_bb1_bb1_off, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]],
            ],
        )

        sample_y_true = np.array(
            [
                [bb1, top_left_bounding_box, far_away_box],
                [bb1, top_left_bounding_box, far_away_box],
            ],
        )
        sample_y_pred = np.array(
            [bb1_off_by_1_pred, top_left_bounding_box, another_far_away_pred],
        )

        result = iou_lib.compute_iou(sample_y_true, sample_y_pred, "yxyx")
        self.assertAllClose(expected_result, result)

    def test_unbatched_boxes1_batched_boxes2(self):
        bb1 = [100, 101, 200, 201]
        bb1_off_by_1_pred = [101, 102, 201, 202]
        iou_bb1_bb1_off = 0.96097656633
        top_left_bounding_box = [0, 2, 1, 3]
        far_away_box = [1300, 1400, 1500, 1401]
        another_far_away_pred = [1000, 1400, 1200, 1401]

        # Rows represent predictions, columns ground truths
        expected_result = np.array(
            [
                [[iou_bb1_bb1_off, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]],
                [[iou_bb1_bb1_off, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]],
            ],
        )

        sample_y_true = np.array(
            [
                [bb1, top_left_bounding_box, far_away_box],
            ],
        )
        sample_y_pred = np.array(
            [
                [
                    bb1_off_by_1_pred,
                    top_left_bounding_box,
                    another_far_away_pred,
                ],
                [
                    bb1_off_by_1_pred,
                    top_left_bounding_box,
                    another_far_away_pred,
                ],
            ],
        )

        result = iou_lib.compute_iou(sample_y_true, sample_y_pred, "yxyx")
        self.assertAllClose(expected_result, result)
