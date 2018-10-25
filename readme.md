# What is this program.
See wiki.  
https://bitbucket.org/datasectiondl/parse_ecgpc_alpha/wiki/Home


# Settings
change .env file.

```txt
vi .env

ex)
INPUT=exams/
OUTPUT=output/output_docker
SUMMARY=summary.json
```


## What is SUMMARY

A file to save relations among TEP, image for observation and each wave txt file.  
You can use the file in the repo, "analysis_ecgpc_alpha".


# Execute with docker-compose

```bash
docker-compose up
```


# Summary syntax
```json
{"summary": 
  [
    {
	  "image_file": image_file_path,
	  "text_files": [text_files_list],
	  "original_file": original_tep_file_path
	}
  ]...
}
```