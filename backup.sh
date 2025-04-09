#!/bin/bash

# Variables
WEB_DIR="/var/www/html"
BACKUP_DIR="/backup"
DB_NAME="mydb"
DB_USER="root"
DB_PASS="yourpassword"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
LOGFILE="/var/log/backup.log"

# Create backup directory if not exists
mkdir -p "$BACKUP_DIR"

# Backup web files
tar -czf "$BACKUP_DIR/web_$DATE.tar.gz" "$WEB_DIR"

# Backup database
mysqldump -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$BACKUP_DIR/db_$DATE.sql"

# Log the output
echo "$DATE - Backup completed: web and db saved." >> "$LOGFILE"
