#!/bin/bash

mkdir /compute_scratch/${job_id}

cd /job/executable/data/

mv * /compute_scratch/${job_id}/
