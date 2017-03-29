BatchUploadTools [![Build Status](https://travis-ci.org/lokal-profil/BatchUploadTools.svg?branch=master)](https://travis-ci.org/lokal-profil/BatchUploadTools)
=======

An attempt of unifying the various tools for batch uploads under one repo.

Heavily based on the [LSH](https://github.com/lokal-profil/LSH) repo


## To install

You can install `BatchUploadTools` via `pip` using:
`pip install git+https://github.com/lokal-profil/BatchUploadTools.git`

If you are not already using the developer version of pywikibot (3.0-dev) you
will have to add the  `--process-dependency-links` flag to the pip command.

If it is your first time running pywikibot you will also have to set up a
`user-config.py` file.

## Running as a different user:

To run as a different user to your standard pywikibot simply place a
modified `user-config.py`-file in the top directory.

To use a different user for a particular batchupload place the `user-config.py`
in the subdirectory and run the script with `-dir:<sub-directory>`.

## When creating a new batch upload

Extend `make_info` to create own methods for reading and processing the indata.
Any method marked as abstract must be implemented locally. You can make use
of the various helper functions in the other classes.

Alternatively you can make use of only the prep-uploader/uploader tools by
creating your own indata file. This must then be a json file where each image
is represented by a dictionary entry with the *original filename* (without
the file extension) as the key and the following values:
 - `info`: the wikitext to be used on the description page (e.g. an information
   template)
 - `filename`: the filename to be used on Commons (without the file extension)
 - `cats`: a list of content categories (without "Category" prefix)
 - `meta_cats`: a list of meta categories (without "Category" prefix)

## Protocol for a batch upload

1. Load indata to a dictionary
2. Process the indata to generate mapping lists
3. Load the indata and the mappings to produce a list of original filenames
   (of media files) and their final filenames as well as json holding the
   following for each file:
    - Maintenance categories
    - Content categories
    - File description
    - Output filename
    - Input filename (as key)
4. Run the prep-uploader to rename the media files and create the text file
   for the associated file description page.
5. Run the uploader to upload it all

## Usage example:

For usage examples see [lokal-profil/upload_batches](https://github.com/lokal-profil/upload_batches).
In particular SMM-images.

## Handling upload errors

In most cases it is worth doing a second pass over any files which trigger an
error since it is either a temporary hick-up or the file was actually uploaded.
Below follows a list of of common errors and what to do about them (when known).

1. `stashedfilenotfound: Could not find the file in the stash.` Seems to
   primarilly be due to larger files. Solution: Manually upload this using
   Upload Wizard.
2. `stashfailed: This file contains HTML or script code that may be erroneously interpreted by a web browser.`
   Either you really have html tags in your exif data or you have triggered [T143610](https://phabricator.wikimedia.org/T143610).
   Smaller files can often be uploaded unchunked (slow).
3. `stashfailed: Cannot upload this file because Internet Explorer would detect it as "$1", which is a disallowed and potentially dangerous file type`
   No clue yet. See [T147720](https://phabricator.wikimedia.org/T147720)
