##########
Change Log
##########

All notable changes to this project are documented in this file.


==========
Unreleased
==========

Added
-----
* ``get_or_run`` method to ``Resolwe`` class to return matching
  object if already exists, otherwise create it

Changed
-------
* Include all necessary files for running the tests in source distribution
* Exclude tests from built/installed version of the package
* File field passed to ``run`` function can be url address

Fixed
-----
* Fix ``files`` and ``download`` methods in ``collection`` resource to
  work with hydrated list of Data objects
* ``inputs`` and ``collections`` are automatically dehydrated if whole
  objects are passed to ``run`` function
* Set chunk size for uploading files to 8MB
* Original value of ``input`` parameter is kept when running ``run``
  funtion


==================
1.4.0 - 2016-10-19
==================

Added
-----
* ``sample`` and ``presample`` properties to ``data`` resource
* ``add_data`` and ``remove_data`` methods on collection and sample
  resource for adding data objects to them

Changed
-------
* Auto-add 'output' prefix to ``field_name`` parameter for
  downloading files
* Auto-wrapp ``list:*`` fields into list if they are not already
* Data objects in ``data`` field on collection resource are
  automatically hydrated
* ``data`` attribute on collection/sample resource is now read
  only

Fixed
-----
* Fix the descriptor to match the updated sample and reads descriptor schemas


==================
1.3.7 - 2016-10-05
==================

Added
-----
* Check PEP 8 and PEP 257
* Feature resource and resolwe-update-kb script
* Remove resources with the delete() method
* Create and update resources with the save() method
* Validate read only and update protected fields

Changed
-------
* Remove resolwe-upload-reads-batch script
* Add option to enable logger (verbose reporting) in scripts

Fixed
-----
* Fix resolwe-upload-reads script
* Rename ResolweQuerry to ResolweQuery
* Add missing HTTP referer header


==================
1.3.6 - 2016-08-15
==================

Fixed
-----
* Fix descriptor in the sequp script


==================
1.3.5 - 2016-08-04
==================

Changed
-------
* Improved documentation organization and text


==================
1.3.4 - 2016-08-01
==================

Added
-----
* Support logging
* Add process resource
* Docs: Getting started and writing pipelines
* Add unit tests for almost all modules of the package
* Support ``list:basic:file:`` field
* Support managing Samples on presample endpoint

Changed
-------
* Track test coverage with Codecov
* Modify scripts.py to work with added features


==================
1.3.3 - 2016-05-18
==================

Fixed
-----
* Fix docs examples
* Fix error handling in ID/slug resource query


==================
1.3.2 - 2016-05-17
==================

Fixed
-----
* Fix docs use case


==================
1.3.1 - 2016-05-16
==================

Added
-----
* Writing processes docs

Changed
-------
* Rename ``upload`` method to ``run`` and refactor to run any process
* Move ``downlad`` method from ``resolwe.py`` to ``resource/base.py``


==================
1.3.0 - 2016-05-10
==================

Added
-----
* Endpoints ``data``, ``sample`` and ``collections`` in ``Resolwe`` class
* ``ResolweQuery`` class with ``get`` and ``filter`` methods
* ``Sample`` class with ``files`` and ``download`` methods
* Tox configuration for running tests
* Travis configuration for automated testing

Changed
-------
* Rename resolwe_api to resdk
* Add ``data``, ``sample``, ``collections`` to ``Resolwe`` class and create
  ``ResolweQuery`` class
* Move ``data.py``, ``collections.py`` ... to ``resources`` folder
* Remove ``collection``, ``collection_data`` and ``data`` methods from
  ``Resolwe`` and from tests.

Fixed
-----
* ``Sequp`` for paired-end data
* Pylint & PEP8 formatting
* Packaging - add missing files and packages


==================
1.2.0 - 2015-11-17
==================

Fixed
-----
* Documentation supports new namespace.
* Scripts support new namespace.


==================
1.1.2 - 2015-05-27
==================

Changed
-------
* Use urllib.urlparse.
* Slumber version bump (>=0.7.1).


==================
1.1.1 - 2015-04-27
==================

Added
-----
* Query data directly.

Changed
-------
* Query projects by slug or ID.

Fixed
-----
* Renamed genapi module in README.
* Renamed some methods for fetching resources.


==================
1.1.0 - 2015-04-27
==================

Changed
-------
* Renamed genesis-genapi to genesis-pyapi.
* Renamed genapi to genesis.
* Refactored API architecture.


==================
1.0.3 - 2015-04-22
==================

Fixed
-----
* Fix not in cache bug at download.


==================
1.0.2 - 2015-04-22
==================

Added
-----
* Universal flag set in setup.cfg.

Changed
-------
* Docs updated to work for recent changes.


==================
1.0.1 - 2015-04-21
==================

Added
-----
* Added label field to annotation.

Fixed
-----
* URL set to dictyexpress.research.bcm.edu by default.
* Id and name attribute are set on init.


==================
1.0.0 - 2015-04-17
==================

Changed
-------
* Upload files in chunks of 10MB.

Fixed
-----
* Create resources fixed for SSL.
