1.	MEMBUAT ORGANIZATION PADA GITHUB
	klik tanda panah ke bawah di samping kanan user di github
    pilih lalu your organization 
2.	TUGAS MENAMBAHKAN ANGGOTA TEAM
	masuk kedalam repository organization yang telah dibuat (membuat repository terlebih dahulu di dalam organization sama seperti membuat repositoty biasa), klik bagian setting lalu pilih collabolator dan pilih add people. Setelah memilih anggota team diharapkan mengirim link invitetion pada orang yang di jadikan anggota.
3.	PUSH FIRST COMMIT
	Sama seperti melakukan push pertama.
4.	PULL REQUEST
	terdapat dua cara yaitu Fork & Pull Model dan Share Repository Model
	** membuka bagian organization -lalu buka repository pilih fork dibagian kanan atas.
	** akan  muncul " Where should we fork code?"
	** pilih akun github kita untuk menyalin.
	** selanjutnya mengclone repository yang di salin dengan cara :
	-------
	donie@donie-ThinkPad-T430:~$ git clone https://github.com/oksipindonesia/Ajakan-Bergabung.git
	Cloning into 'Ajakan-Bergabung'...
	remote: Enumerating objects: 13, done.
	remote: Counting objects: 100% (13/13), done.
	remote: Compressing objects: 100% (10/10), done.
	remote: Total 13 (delta 1), reused 12 (delta 0), pack-reused 0
	Unpacking objects: 100% (13/13), 20.26 KiB | 399.00 KiB/s, done.
	-------
5.	Membuat branch (cabang baru)
	Adapun caranya sebagai berikut : 
	-----
	Melakukan edit git checkout -b pull. pull adalah nama branch yang saya buat. maka akan muncul
	Switched to a new branch 'pull'
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git add .
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git commit -m "information added in readme"
	On branch pull
	nothing to commit, working tree clean
	cabangnya harus sebagai master.
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git checkout master
	error: pathspec 'master' did not match any file(s) known to git
	jika mengalami eror seperti saya maka harus merubah terlebih dahulu ke main dengan cara
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git branch -M master
	lalu chek lagi apakah sudah masuk ke master atau belum dengan cara
	git branch
	jika sudah muncul seperti di bawah ono maka sudah:
 	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git branch
	* master
	pull
	selanjutnya lakukan :
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git remote -v
	origin	https://github.com/oksipindonesian/ajakan-bergabung.git (fetch)
	origin	https://github.com/oksipindonesian/ajakan-bergabung.git (push)
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git fetch https://github.com/oksipindonesian/ajakan-bergabung.git
	From https://github.com/oksipindonesian/ajakan-bergabung.git
	* branch            HEAD       -> FETCH_HEAD
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git push https://github.com/oksipindonesian/ajakan-bergabung.git
	Username for 'https://github.com': oksipjogja
	Password for 'https://oksipjogja@github.com': 
	Total 0 (delta 0), reused 0 (delta 0)
	remote: 
	remote: Create a pull request for 'master' on GitHub by visiting:
	remote:      https://github.com/oksipindonesian/ajakan-bergabung/pull/new/master
	remote: 
	To https://github.com/oksipindonesian/ajakan-bergabung.git
	* [new branch]      master -> master
	donie@donie-ThinkPad-T430:~/ajakan-bergabung~$ git push origin pull
	Username for 'https://github.com': oksipjogja
	Password for 'https://oksipjogja@github.com': 
	Total 0 (delta 0), reused 0 (delta 0)
	remote: 
	remote: Create a pull request for 'pull' on GitHub by visiting:
	remote:      https://github.com/oksipindonesian/ajakan-bergabung/pull/new/pull
	remote: 
	To https://github.com/oksipindonesian/ajakan-bergabung.git
	 * [new branch]      pull -> pull
	-------
6.  MERGING A PULL REQUSET
	Buka repository organization- lalu klil pull request- klik new pull requet- dalam bagian base pilih branch yang kita buat -bagian compare pilih branch main atau master- dan tunggu konfirmasi. gunanya untuk melihat perubahan apa saja yang terjadi di github
7.	Setting Up Travis CI


