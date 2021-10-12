# This file was generated automatically from a frictionless datapackage
#  using frictionless-dataclass.

from dataclasses import dataclass
from typing import Optional, Dict, List, Any

class table_schema_specs_for_c2m2_encoding_of_dcc_metadata:
  '''A complete list of schematic specifications for the resources (TSV table files) that will be used to represent C2M2 DCC metadata prior to ingest into the C2M2 database system'''
  
  @dataclass
  class file:
    '''A stable digital asset'''
    # (string) A CFDE-cleared identifier representing the top-level data space containing this file [part 1 of 2-component composite primary key]
    id_namespace: str = str()
    
    # (string) An identifier representing this file, unique within this id_namespace [part 2 of 2-component composite primary key]
    local_id: str = str()
    
    # (string) The id_namespace of the primary project within which this file was created [part 1 of 2-component composite foreign key]
    project_id_namespace: str = str()
    
    # (string) The local_id of the primary project within which this file was created [part 2 of 2-component composite foreign key]
    project_local_id: str = str()
    
    # (string) A persistent, resolvable (not necessarily retrievable) URI or compact ID permanently attached to this file
    persistent_id: Optional[str] = None
    
    # (datetime) An ISO 8601 -- RFC 3339 (subset)-compliant timestamp documenting this file's creation time: YYYY-MM-DDTHH:MM:SS±NN:NN
    creation_time: Optional[str] = None
    
    # (integer) The size of this file in bytes
    size_in_bytes: Optional[int] = None
    
    # (integer) The total decompressed size in bytes of the contents of this file
    uncompressed_size_in_bytes: Optional[int] = None
    
    # (string) (preferred) SHA-256 checksum for this file [sha256, md5 cannot both be null]
    sha256: Optional[str] = None
    
    # (string) (allowed) MD5 checksum for this file [sha256, md5 cannot both be null]
    md5: Optional[str] = None
    
    # (string) A filename with no prepended PATH information
    filename: Optional[str] = None
    
    # (string) An EDAM CV term ID identifying the digital format of this file (e.g. TSV or FASTQ)
    file_format: Optional[str] = None
    
    # (string) An EDAM CV term ID identifying the type of information stored in this file (e.g. RNA sequence reads)
    data_type: Optional[str] = None
    
    # (string) An OBI CV term ID describing the type of experiment that generated the results summarized by this file
    assay_type: Optional[str] = None
    
    # (string) A MIME type describing this file
    mime_type: Optional[str] = None
    
  @dataclass
  class biosample:
    '''A tissue sample or other physical specimen'''
    # (string) A CFDE-cleared identifier representing the top-level data space containing this biosample [part 1 of 2-component composite primary key]
    id_namespace: str = str()
    
    # (string) An identifier representing this biosample, unique within this id_namespace [part 2 of 2-component composite primary key]
    local_id: str = str()
    
    # (string) The id_namespace of the primary project within which this biosample was created [part 1 of 2-component composite foreign key]
    project_id_namespace: str = str()
    
    # (string) The local_id of the primary project within which this biosample was created [part 2 of 2-component composite foreign key]
    project_local_id: str = str()
    
    # (string) A persistent, resolvable (not necessarily retrievable) URI or compact ID permanently attached to this biosample
    persistent_id: Optional[str] = None
    
    # (datetime) An ISO 8601 -- RFC 3339 (subset)-compliant timestamp documenting this biosample's creation time: YYYY-MM-DDTHH:MM:SS±NN:NN
    creation_time: Optional[str] = None
    
    # (string) An OBI CV term ID describing the type of experiment that generated this biosample
    assay_type: Optional[str] = None
    
    # (string) An UBERON CV term ID used to locate the origin of this biosample within the physiology of its source or host organism
    anatomy: Optional[str] = None
    
  @dataclass
  class subject:
    '''A biological entity from which a C2M2 biosample can be generated'''
    # (string) A CFDE-cleared identifier representing the top-level data space containing this subject [part 1 of 2-component composite primary key]
    id_namespace: str = str()
    
    # (string) An identifier representing this subject, unique within this id_namespace [part 2 of 2-component composite primary key]
    local_id: str = str()
    
    # (string) The id_namespace of the primary project within which this subject was studied [part 1 of 2-component composite foreign key]
    project_id_namespace: str = str()
    
    # (string) The local_id of the primary project within which this subject was studied [part 2 of 2-component composite foreign key]
    project_local_id: str = str()
    
    # (string) A persistent, resolvable (not necessarily retrievable) URI or compact ID permanently attached to this subject
    persistent_id: Optional[str] = None
    
    # (datetime) An ISO 8601 -- RFC 3339 (subset)-compliant timestamp documenting this subject record's creation time: YYYY-MM-DDTHH:MM:SS±NN:NN
    creation_time: Optional[str] = None
    
    # (string) A CFDE CV term categorizing this subject by multiplicity
    granularity: str = str()
    
  @dataclass
  class primary_dcc_contact:
    '''One primary contact person for the Common Fund data coordinating center (DCC, identified by the given project foreign key) that produced this C2M2 instance'''
    # (string) Email address of this DCC contact
    contact_email: str = str()
    
    # (string) Name of this DCC contact
    contact_name: str = str()
    
    # (string) The id_namespace of the project record representing this contact's DCC [part 1 of 2-component composite foreign key]
    project_id_namespace: str = str()
    
    # (string) The local_id of the project record representing this contact's DCC [part 2 of 2-component composite foreign key]
    project_local_id: str = str()
    
    # (string) A very short display label for this contact's DCC
    dcc_abbreviation: str = str()
    
    # (string) A short, human-readable, machine-read-friendly label for this contact's DCC
    dcc_name: str = str()
    
    # (string) A human-readable description of this contact's DCC
    dcc_description: Optional[str] = None
    
    # (string) URL of the front page of the website for this contact's DCC
    dcc_url: str = str()
    
  @dataclass
  class project:
    '''A node in the C2M2 project hierarchy subdividing all resources described by this DCC's C2M2 metadata'''
    # (string) A CFDE-cleared identifier representing the top-level data space containing this project [part 1 of 2-component composite primary key]
    id_namespace: str = str()
    
    # (string) An identifier representing this project, unique within this id_namespace [part 2 of 2-component composite primary key]
    local_id: str = str()
    
    # (string) A persistent, resolvable (not necessarily retrievable) URI or compact ID permanently attached to this project
    persistent_id: Optional[str] = None
    
    # (datetime) An ISO 8601 -- RFC 3339 (subset)-compliant timestamp documenting this project's creation time: YYYY-MM-DDTHH:MM:SS±NN:NN
    creation_time: Optional[str] = None
    
    # (string) A very short display label for this project
    abbreviation: Optional[str] = None
    
    # (string) A short, human-readable, machine-read-friendly label for this project
    name: str = str()
    
    # (string) A human-readable description of this project
    description: Optional[str] = None
    
  @dataclass
  class project_in_project:
    '''Association between a child project and its parent'''
    # (string) ID of the identifier namespace for the parent in this parent-child project pair
    parent_project_id_namespace: str = str()
    
    # (string) The ID of the containing (parent) project
    parent_project_local_id: str = str()
    
    # (string) ID of the identifier namespace for the child in this parent-child project pair
    child_project_id_namespace: str = str()
    
    # (string) The ID of the contained (child) project
    child_project_local_id: str = str()
    
  @dataclass
  class collection:
    '''A grouping of C2M2 files, biosamples and/or subjects'''
    # (string) A CFDE-cleared identifier representing the top-level data space containing this collection [part 1 of 2-component composite primary key]
    id_namespace: str = str()
    
    # (string) An identifier representing this collection, unique within this id_namespace [part 2 of 2-component composite primary key]
    local_id: str = str()
    
    # (string) A persistent, resolvable (not necessarily retrievable) URI or compact ID permanently attached to this collection
    persistent_id: Optional[str] = None
    
    # (datetime) An ISO 8601 -- RFC 3339 (subset)-compliant timestamp documenting this collection's creation time: YYYY-MM-DDTHH:MM:SS±NN:NN
    creation_time: Optional[str] = None
    
    # (string) A very short display label for this collection
    abbreviation: Optional[str] = None
    
    # (string) A short, human-readable, machine-read-friendly label for this collection
    name: Optional[str] = None
    
    # (string) A human-readable description of this collection
    description: Optional[str] = None
    
  @dataclass
  class collection_in_collection:
    '''Association between a containing collection (superset) and a contained collection (subset)'''
    # (string) ID of the identifier namespace corresponding to the top-level C2M2 metadataset containing the superset collection
    superset_collection_id_namespace: str = str()
    
    # (string) The ID of the superset collection
    superset_collection_local_id: str = str()
    
    # (string) ID of the identifier namespace corresponding to the top-level C2M2 metadataset containing the subset collection
    subset_collection_id_namespace: str = str()
    
    # (string) The ID of the subset collection
    subset_collection_local_id: str = str()
    
  @dataclass
  class file_describes_collection:
    '''Association between a summary file and an entire collection described by that file'''
    # (string) Identifier namespace for this file
    file_id_namespace: str = str()
    
    # (string) The ID of this file
    file_local_id: str = str()
    
    # (string) Identifier namespace for this collection
    collection_id_namespace: str = str()
    
    # (string) The ID of this collection
    collection_local_id: str = str()
    
  @dataclass
  class collection_defined_by_project:
    '''(Shallow) association between a collection and a project that defined it'''
    # (string) ID of the identifier namespace corresponding to the top-level C2M2 metadataset containing this collection
    collection_id_namespace: str = str()
    
    # (string) The ID of this collection
    collection_local_id: str = str()
    
    # (string) ID of the identifier namespace corresponding to the top-level C2M2 metadataset containing this project
    project_id_namespace: str = str()
    
    # (string) The ID of this project
    project_local_id: str = str()
    
  @dataclass
  class file_in_collection:
    '''Association between a file and a (containing) collection'''
    # (string) Identifier namespace for this file
    file_id_namespace: str = str()
    
    # (string) The ID of this file
    file_local_id: str = str()
    
    # (string) Identifier namespace for this collection
    collection_id_namespace: str = str()
    
    # (string) The ID of this collection
    collection_local_id: str = str()
    
  @dataclass
  class biosample_in_collection:
    '''Association between a biosample and a (containing) collection'''
    # (string) Identifier namespace for this biosample
    biosample_id_namespace: str = str()
    
    # (string) The ID of this biosample
    biosample_local_id: str = str()
    
    # (string) Identifier namespace for this collection
    collection_id_namespace: str = str()
    
    # (string) The ID of this collection
    collection_local_id: str = str()
    
  @dataclass
  class subject_in_collection:
    '''Association between a subject and a (containing) collection'''
    # (string) Identifier namespace for this subject
    subject_id_namespace: str = str()
    
    # (string) The ID of this subject
    subject_local_id: str = str()
    
    # (string) Identifier namespace for this collection
    collection_id_namespace: str = str()
    
    # (string) The ID of this collection
    collection_local_id: str = str()
    
  @dataclass
  class file_describes_biosample:
    '''Association between a biosample and a file containing information about that biosample'''
    # (string) Identifier namespace for this file
    file_id_namespace: str = str()
    
    # (string) The ID of this file
    file_local_id: str = str()
    
    # (string) Identifier namespace for this biosample
    biosample_id_namespace: str = str()
    
    # (string) The ID of this biosample
    biosample_local_id: str = str()
    
  @dataclass
  class file_describes_subject:
    '''Association between a subject and a file containing information about that subject'''
    # (string) Identifier namespace for this file
    file_id_namespace: str = str()
    
    # (string) The ID of this file
    file_local_id: str = str()
    
    # (string) Identifier namespace for this subject
    subject_id_namespace: str = str()
    
    # (string) The ID of this subject
    subject_local_id: str = str()
    
  @dataclass
  class biosample_from_subject:
    '''Association between a biosample and its source subject'''
    # (string) Identifier namespace for this biosample
    biosample_id_namespace: str = str()
    
    # (string) The ID of this biosample
    biosample_local_id: str = str()
    
    # (string) Identifier namespace for this subject
    subject_id_namespace: str = str()
    
    # (string) The ID of this subject
    subject_local_id: str = str()
    
  @dataclass
  class biosample_disease:
    '''Association between a C2M2 biosample and a disease known to be associated with that biosample'''
    # (string) Identifier namespace for this biosample
    biosample_id_namespace: str = str()
    
    # (string) The ID of this biosample
    biosample_local_id: str = str()
    
    # (string) A Disease Ontology CV term ID describing this disease
    disease: str = str()
    
  @dataclass
  class subject_disease:
    '''Association between a C2M2 subject and a disease positively identified in that subject'''
    # (string) Identifier namespace for this subject
    subject_id_namespace: str = str()
    
    # (string) The ID of this subject
    subject_local_id: str = str()
    
    # (string) A Disease Ontology CV term ID describing this disease
    disease: str = str()
    
  @dataclass
  class subject_role_taxonomy:
    '''Trinary association linking IDs representing (1) a subject, (2) a subject_role (a named organism-level constituent component of a subject, like 'host', 'pathogen', 'endosymbiont', 'taxon detected inside a microbiome subject', etc.) and (3) a taxonomic label (which is hereby assigned to this particular subject_role within this particular subject)'''
    # (string) Identifier namespace for this subject
    subject_id_namespace: str = str()
    
    # (string) The ID of this subject
    subject_local_id: str = str()
    
    # (string) The ID of the role assigned to this organism-level constituent component of this subject
    role_id: str = str()
    
    # (string) An NCBI Taxonomy Database ID identifying this taxon
    taxonomy_id: str = str()
    
  @dataclass
  class assay_type:
    '''List of Ontology for Biomedical Investigations (OBI) CV terms used to describe types of experiment that generate C2M2 biosamples or results stored in C2M2 files'''
    # (string) An OBI CV term
    id: str = str()
    
    # (string) A short, human-readable, machine-read-friendly label for this OBI term
    name: str = str()
    
    # (string) A human-readable description of this OBI term
    description: Optional[str] = None
    
    # (array) A list of synonyms for this term as identified by the OBI metadata
    synonyms: Optional[List[Any]] = None
    
  @dataclass
  class ncbi_taxonomy:
    '''List of NCBI Taxonomy Database IDs identifying taxa used to describe C2M2 subjects'''
    # (string) An NCBI Taxonomy Database ID identifying a particular taxon
    id: str = str()
    
    # (string) The phylogenetic level (e.g. species, genus) assigned to this taxon
    clade: str = str()
    
    # (string) A short, human-readable, machine-read-friendly label for this taxon
    name: str = str()
    
    # (string) A human-readable description of this taxon
    description: Optional[str] = None
    
    # (array) A list of synonyms for this taxon as identified by the NCBI Taxonomy DB
    synonyms: Optional[List[Any]] = None
    
  @dataclass
  class anatomy:
    '''List of Uber-anatomy ontology (UBERON) CV terms used to locate the origin of a C2M2 biosample within the physiology of its source or host organism'''
    # (string) An UBERON CV term
    id: str = str()
    
    # (string) A short, human-readable, machine-read-friendly label for this UBERON term
    name: str = str()
    
    # (string) A human-readable description of this UBERON term
    description: Optional[str] = None
    
    # (array) A list of synonyms for this term as identified by the UBERON metadata
    synonyms: Optional[List[Any]] = None
    
  @dataclass
  class file_format:
    '''List of EDAM CV 'format:' terms used to describe formats of C2M2 files'''
    # (string) An EDAM CV format term
    id: str = str()
    
    # (string) A short, human-readable, machine-read-friendly label for this EDAM format term
    name: str = str()
    
    # (string) A human-readable description of this EDAM format term
    description: Optional[str] = None
    
    # (array) A list of synonyms for this term as identified by the EDAM metadata
    synonyms: Optional[List[Any]] = None
    
  @dataclass
  class data_type:
    '''List of EDAM CV 'data:' terms used to describe data in C2M2 files'''
    # (string) An EDAM CV data term
    id: str = str()
    
    # (string) A short, human-readable, machine-read-friendly label for this EDAM data term
    name: str = str()
    
    # (string) A human-readable description of this EDAM data term
    description: Optional[str] = None
    
    # (array) A list of synonyms for this term as identified by the EDAM metadata
    synonyms: Optional[List[Any]] = None
    
  @dataclass
  class disease:
    '''List of Disease Ontology terms used to describe diseases associated with C2M2 subjects or biosamples'''
    # (string) A Disease Ontology term
    id: str = str()
    
    # (string) A short, human-readable, machine-read-friendly label for this Disease Ontology term
    name: str = str()
    
    # (string) A human-readable description of this Disease Ontology term
    description: Optional[str] = None
    
    # (array) A list of synonyms for this term as identified by the Disease Ontology metadata
    synonyms: Optional[List[Any]] = None
    
  @dataclass
  class id_namespace:
    '''A table listing identifier namespaces registered by the DCC submitting this C2M2 instance'''
    # (string) ID of this identifier namespace
    id: str = str()
    
    # (string) A very short display label for this identifier namespace
    abbreviation: Optional[str] = None
    
    # (string) A short, human-readable, machine-read-friendly label for this identifier namespace
    name: str = str()
    
    # (string) A human-readable description of this identifier namespace
    description: Optional[str] = None
    
