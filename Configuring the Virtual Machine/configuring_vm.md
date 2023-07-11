# Configuring  the Virtual Machine

Creating a virtual machine is just the first step towards building an efficient and effective development environment. 

To unlock its full potential, you need to install the right tools and software. In this tutorial, we'll take you through the process of installing two of the most powerful tools in the data engineering toolkit - Anaconda and Docker - on the virtual machine we created in our last tutorial. 

By the end of this tutorial, you'll have a fully functional development environment that's optimized for data engineering workflows. So, let's get started!


**Installing Anaconda**

* Visit [Anaconda's website](https://www.anaconda.com/download) and copy the link to Linux 64-Bit Installer.

    ![alt text](img/anaconda1.png)  

* Download the file in the VM:

```bash
 wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
```

* Run the downloaded file:

  ```
  bash Anaconda3-2023.03-1-Linux-x86_64.sh
  ```

  **Take Note!**

  - Keep pressing Enter to scroll down and enter yes to accept the license terms.

  -  Press Enter to confirm the default location.

  -  Enter yes to run the conda init when asked.

  -  After the installation is complete, run the command ```source .bashrc ```to apply the changes to the ```.bashrc ```file. Alternatively, you can log out of the session using the ```logout``` command and then ssh back in for the changes to take effect.


  **Installing Docker**

  Run the following commands:

  ```bash
  sudo apt-get update

  sudo apt-get upgrade

  sudo apt-get install docker.io

  ```

 *This will install docker but you'll not be able to run it without ```sudo```. It'll throw a permission denied error*

  To run docker without ```sudo```, run the following commands:


  ```bash
  sudo groupadd docker

  sudo gpasswd -a $USER docker

  sudo service docker restart
  ```

  The  commands   above are useful for managing access to the Docker daemon and ensuring that Docker commands can be run safely and securely by non-root users.

  > 1. ```sudo groupadd docker```: This command creates a new group called "docker". This group will be used to manage access to the Docker daemon, which is the background service that runs the Docker containers. By default, only users with administrative privileges can access the Docker daemon. By adding a user to the "docker" group, they can run Docker commands without having to use sudo.

> 2. ```sudo gpasswd -a $USER docker```: This command adds the current user (represented by the $USER variable) to the "docker" group. This grants the user permission to run Docker commands as a non-root user, which is generally safer than running Docker commands with root privileges.

> 3. ```sudo service docker restart```: This command restarts the Docker service. This is necessary to apply changes made to the Docker configuration, such as adding a user to the "docker" group. After the service is restarted, the user can run Docker commands without having to log out and log back in again.


[Refer to this link ](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md) for more  explanation of the above commands.


Log out of the ssh session and log back in to re-evaluate the group memberships and run the ```docker run hello-world``` command.


![alt text](img/docker.png)  


**Installing docker-compose**

* Go to the docker-compose [GitHub repo](https://github.com/docker/compose)  and under the latest release, find the ```"docker-compose-linux-x86_64"``` asset and copy its link.

* Create a new bin folder in VM and download the asset into it:

```bash
      mkdir bin

      cd bin

      wget https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -O docker-compose
```

* This will create a new file docker-compose in the bin folder.

* Make this file executable:

```bash
chmod +x docker-compose
```

*This command adds executable permissions to the downloaded file "docker-compose", making it possible to run this file as a program.*

* Now, add the bin folder to the path:

 > *adding the bin directory to the system PATH variable is done so that the Docker Compose binary can be executed from any directory on the system.*

  * Go to the home directory: ```cd```

  * Open the .bashrc file: ```nano .bashrc```

  * Paste the following to the end of the ```.bashrc``` file:

```bash
 export PATH="${HOME}/bin:${PATH}"
```

* Press Ctrl+O > enter > Ctrl+X

* Run source .bashrc for the changes to take effect.




**Check the version of the docker composer**

  ```bash
 docker-compose version
```

![alt text](img/docker2.png)  

Now, you have docker-compose installed as well.






  