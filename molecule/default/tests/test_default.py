import testinfra

def test_nfsstat_installed(host):
    command = host.run("nfsstat --version")

    assert command.rc == 0
    assert "nfsstat" in command.stdout

def test_fstab_contains_nfs_mount(host):
    fstab = host.file("/etc/fstab")
    assert fstab.exists
    assert fstab.contains("your-nfs-server:/path /mnt/nfs nfs")  # Replace with your actual NFS server, mount point, and options