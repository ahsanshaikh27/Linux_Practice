# DevOps Backup Script

This is a simple shell script to automate the backup of web files and a MySQL database.  
Useful for small web projects or WordPress backups.

## Features
- Backup web directory (`/var/www/html`)
- Backup MySQL database
- Log backups to `/var/log/backup.log`

## Usage

1. Update the database credentials inside `backup.sh`.
2. Make the script executable:
   ```bash
   chmod +x backup.sh
