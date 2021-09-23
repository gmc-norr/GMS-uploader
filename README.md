# GMS-uploader
GUI utility for uploading sequence and metadata to the NGP. Under development = there will be bugs.


GMS-uploader objectives:
* Construction of metadata files to go along with sequencing data
  * Enforces structure and prevents errors
    * Many fields are restricted to accepted values and can only entered via comboboxes etc.
  * Data validation before upload
  * Should (hopefully) be simpler and faster than using for example MS Excel
    * Simple entering of data is supported by using arrow-keys for moving around, autopopulation, fill-down of cells, and cut-and-paste from other sources using ctrl-c, ctrl-v 
  * Saves as json
* Upload to the NGP
  * Upload of data using HCP Interface (S3)

## Introduction

The GMS-uploader is a GUI tool intended to simplify contruction of metadata files that go along with sequencing data for upload to the Swedish National Genomics Platform.

The GMS-uploader uses [HCP Interface](https://github.com/genomic-medicine-sweden/HCPInterface) which in turn heavily depends on [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) and uses the S3 protocol. It can therefore be used in any setting where S3 is used.   

## Installation

Download from the [release](https://github.com/genomic-medicine-sweden/GMS-uploader/releases), unpack into a suitable location, and run by double-clicking the gms-uploader.exe binary. It is now distributed only as a folder structure, future releases will probably be using [installForge](https://installforge.net/) .

## Usage

* Go into the preferences view by clicking the preferences button (cogs), and enter all necessary information, including:
  * Data_root_path: a convenience setting to simplify browsing for new data using the sequence file dialog.
  * Metadata_save_path: a folder where metadata json-files should be saved
  * Pseudo_ID_filepath: a textfile which stores previously generated pseudo_id numbers. They constitute serial numbers and are auto-incremented for each sample.
  * Submitter: the name of the submitter
  * AWS_key_id: the aws key id, for connecting with the hcp
  * AWS_secret_key: the aws secret key, for connecting with the hcp
  * Endpoint: the hcp url
  * HCP_buckets: the actual bucket at the hcp to be used
  * Lab: submitting lab (your lab!)
  * Sequencing_technology: The technology being used
  * Host: What kind of sample is it?
  * Library_method: What library method was used?
  * Region: Which regions should you be allowed to choose from?
  * Selection_criterion: Which criteria should you be allowed to choose from?
  * Patient_sex
  * Passage_details_history 
  * Type
  * Patient_status

* Settings are saved in your windows registry, so you should not have to enter them again.
  * It should be noted that the AWS secret key is currently also saved in clear text, which is unsafe. A solution to this should be found. However, the HCP can only be accessed via Sjunet and the windows registry can only be accessed if you have access to the computer.   

* Import sequence files you would like to upload
  * By convention, it is assumed that the first part of the filename (before '_') represents the internal lab id, which will be used as unique id for the sample.
  * Either drag-and-drop sequence files you would like to upload into the utility, or import using the import dialog button (with a DNA spiral on it).
  * After files have been imported, start populating the matrix
  * After matrix is populated, pressing the upload button the data is validated and uploaded using HCP Interface



