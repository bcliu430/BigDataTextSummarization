# Fetch data from the Hadoop server

The script `fetch_data.sh` downloads the data from the Hadoop server. Running the script downloads a directory called `team10` to the current working directory.

The script currently uses `sshpass` to supply the password to the `scp` command. `sshpass` can be installed using `brew` or `apt-get`.
