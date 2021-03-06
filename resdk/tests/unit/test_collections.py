"""
Unit tests for resdk/resources/collection.py file.
"""
# pylint: disable=missing-docstring, protected-access

import unittest

import six

from mock import patch, MagicMock

from resdk.resources.collection import BaseCollection, Collection, get_collection_id
from resdk.resources.sample import Sample, get_sample_id
from resdk.tests.mocks.data import DATA_SAMPLE

DATA0 = MagicMock(**{'files.return_value': [], 'id': 0})

DATA1 = MagicMock(**{'files.return_value': ['reads.fq', 'arch.gz'], 'id': 1})

DATA2 = MagicMock(**{'files.return_value': ['outfile.exp'], 'id': 2})


class TestBaseCollection(unittest.TestCase):

    @patch('resdk.resources.collection.BaseCollection', spec=True)
    def test_init(self, collection_mock):
        collection_mock.configure_mock(endpoint="fake_endpoint")
        BaseCollection.__init__(collection_mock, id=1, resolwe=MagicMock())

    def test_data(self):
        collection = Collection(id=1, resolwe=MagicMock())

        # test setting data attribute
        collection.data = [1, 2, 3]
        self.assertEqual(collection._data, [1, 2, 3])
        self.assertEqual(collection._data_hydrated, False)

        # test getting data attribute
        collection.resolwe.data.filter = MagicMock(return_value=['data_1', 'data_2', 'data_3'])
        self.assertEqual(collection.data, ['data_1', 'data_2', 'data_3'])
        self.assertEqual(collection._data_hydrated, True)

        # test caching data attribute
        self.assertEqual(collection.data, ['data_1', 'data_2', 'data_3'])
        self.assertEqual(collection._data_hydrated, True)
        self.assertEqual(collection.resolwe.data.filter.call_count, 1)

    @patch('resdk.resources.collection.BaseCollection', spec=True)
    def test_data_types(self, collection_mock):
        get_mock = MagicMock(**{'get.return_value': DATA_SAMPLE[0]})
        api_mock = MagicMock(**{'data.return_value': get_mock})
        collection_mock.configure_mock(data=[1, 2], resolwe=MagicMock(api=api_mock))

        types = BaseCollection.data_types(collection_mock)
        self.assertEqual(types, [u'data:reads:fastq:single:'])

    @patch('resdk.resources.collection.BaseCollection', spec=True)
    def test_files(self, collection_mock):
        collection_mock.configure_mock(data=[DATA1, DATA2], resolwe=" ")

        flist = BaseCollection.files(collection_mock)
        self.assertEqual(set(flist), set(['arch.gz', 'reads.fq', 'outfile.exp']))

    @patch('resdk.resources.collection.BaseCollection', spec=True)
    def test_print_annotation(self, collection_mock):
        with self.assertRaises(NotImplementedError):
            BaseCollection.print_annotation(collection_mock)


class TestBaseCollectionDownload(unittest.TestCase):

    @patch('resdk.resources.collection.BaseCollection', spec=True)
    def test_file_type(self, collection_mock):
        collection_mock.configure_mock(data=[DATA0, DATA2], resolwe=MagicMock())
        BaseCollection.download(collection_mock, file_type='output.exp')
        flist = [u'2/outfile.exp']
        collection_mock.resolwe._download_files.assert_called_once_with(flist, None)

        # Check if ok to also provide ``output_field`` that does not start with 'output'
        collection_mock.reset_mock()
        collection_mock.configure_mock(data=[DATA1, DATA0], resolwe=MagicMock())
        BaseCollection.download(collection_mock, file_type='fastq')
        flist = [u'1/reads.fq', u'1/arch.gz']
        collection_mock.resolwe._download_files.assert_called_once_with(flist, None)

    @patch('resdk.resources.collection.BaseCollection', spec=True)
    def test_bad_file_type(self, collection_mock):
        message = "Invalid argument value `file_type`."
        with six.assertRaisesRegex(self, ValueError, message):
            BaseCollection.download(collection_mock, file_type=123)


class TestCollection(unittest.TestCase):

    @patch('resdk.resources.collection.Collection', spec=True)
    def test_collection_init(self, collection_mock):
        collection_mock.configure_mock(endpoint="fake_endpoint")
        Collection.__init__(collection_mock, id=1, resolwe=MagicMock())

    @patch('resdk.resources.collection.Collection', spec=True)
    def test_collection_print_ann(self, collection_mock):
        with self.assertRaises(NotImplementedError):
            Collection.print_annotation(collection_mock)

    def test_get_collection_id(self):
        collection = Collection(id=1, resolwe=MagicMock())
        collection.id = 1  # this is overriden when initialized
        self.assertEqual(get_collection_id(collection), 1)

        self.assertEqual(get_collection_id(2), 2)


class TestSample(unittest.TestCase):

    @patch('resdk.resources.sample.Sample', spec=True)
    def test_sample_init(self, sample_mock):
        sample_mock.configure_mock(endpoint="fake_endpoint")
        Sample.__init__(sample_mock, id=1, resolwe=MagicMock())

    @patch('resdk.resources.sample.Sample', spec=True)
    def test_sample_print_annotation(self, sample_mock):
        with self.assertRaises(NotImplementedError):
            Sample.print_annotation(sample_mock)

    @patch('resdk.resources.sample.Sample', spec=True)
    def test_update_descriptor(self, sample_mock):
        sample_mock.configure_mock(id=42, api=MagicMock())
        Sample.update_descriptor(sample_mock, {'field': 'value'})
        sample_mock.api(42).patch.assert_called_once_with({u'descriptor': {'field': 'value'}})

    @patch('resdk.resources.sample.Sample', spec=True)
    def test_confirm_is_annotated(self, sample_mock):
        sample_mock.configure_mock(endpoint='anything but presample')
        with self.assertRaises(NotImplementedError):
            Sample.confirm_is_annotated(sample_mock)

        sample_mock.configure_mock(endpoint='presample', id=42,
                                   api=MagicMock(), logger=MagicMock())
        Sample.confirm_is_annotated(sample_mock)
        sample_mock.api(42).patch.assert_called_once_with({'presample': False})

    def test_get_sample_id(self):
        sample = Sample(id=1, resolwe=MagicMock())
        sample.id = 1  # this is overriden when initialized
        self.assertEqual(get_sample_id(sample), 1)

        self.assertEqual(get_sample_id(2), 2)


if __name__ == '__main__':
    unittest.main()
