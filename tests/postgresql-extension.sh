#!/bin/bash

psql -d quay -U postgres -c 'CREATE EXTENSION IF NOT EXISTS pg_trgm'
