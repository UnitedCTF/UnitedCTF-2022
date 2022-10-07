# netcat

**`Author:`** [hfz](https://github.com/hfz1337)

## Description

(French will follow)

This challenge serves as an introduction to `netcat`.  
`netcat` is a computer program that we typically use to establish TCP (or UDP) connections with remote servers.  
In the offensive security world, it is often used to (among other things):

- Transfer files from one machine to another;
- Gain a reverse shell or a bind shell on the target machine;
- Connect to network services (SMTP, FTP, etc.), and of course, this includes **CTF challenges**.

### **`#`** Installing `netcat` on Debian-based Linux distributions
```bash
sudo bash -c "apt-get update && apt-get -y install netcat"
```

### **`#`** Installing `netcat` on other platforms
Visit https://nmap.org/download to install both `nmap` (you won't need it in the CTF) and `ncat` (an improved version of the traditional `netcat`).

After install `netcat`, run the below command to get your flag!

---

Ce défi sert d'introduction à l'utilisation de `netcat`.  
`netcat` est un programme informatique que nous utilisons généralement pour établir des connexions TCP (ou UDP) avec des serveurs distants.  
Dans le monde de la sécurité offensive, il est souvent utilisé pour (entre autres):

- Transférer des fichiers d'une machine à une autre;
- Obtenir un reverse shell ou un bind shell sur la machine cible;
- Se connecter à des services réseau (SMTP, FTP, etc.), et bien sûr, cela inclut les défis **CTF**.

### **`#`** Installation de `netcat` sur les distributions Linux basées sur Debian
```bash
sudo bash -c "apt-get update && apt-get -y install netcat"
```

### **`#`** Installation de `netcat` sur les autres plateformes
Visite https://nmap.org/download pour installer à la fois `nmap` (vous n'en aurez pas besoin dans le CTF) et `ncat` (une version améliorée de `netcat`).

Après avoir installé `netcat`, exécute la commande ci-dessous pour obtenir ton flag !

## Solution

Solution of the challenge can be found [here](solution/).
