B
    =cG\��  �               @   s   d dl Z ee �d�� dS )�    Ns�?  �               @   sx  d Z ddlZddlmZ ddlmZ ddlm	Z	 ddl
ZddlZddlZddlZddlmZ dZdZd	Zd
ZdZdZdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Z d!d"� Z!d#d$� Z"d%d&� Z#d'd(� Z$d)d*� Z%d+d,� Z&d-d.� Z'd/d0� Z(d1d2� Z)d3d4� Z*d5d6� Z+d7d8� Z,d9d:� Z-e.d;k�rtye�/d<� W n e0k
�rZ   Y nX y
e �  W n   Y nX dS )=u�  













“Lelaki yang mencuri dan wanita yang mencuri,potonglah tangan keduanya (sebagai) pembalasan bagi apa yang mereka kerjakan dan sebagai siksaan dari Allah.
Dan Allah Maha Perkasa lagi Maha Bijaksana.
Maka barangsiapa bertaubat (di antara pencuri-pencuri itu) sesudah melakukan kejahatan itu dan memperbaiki diri,
maka sesungguhnya Allah menerima taubatnya.
Sesungguhnya Allah Maha Pengampun lagi Maha Penyayang.”

(QS. Al-Maidah: 38-39)
































�    N)�BeautifulSoup)�Thread)�MP3)�sleepz[92mz[91mz[97mz[95mz[90mz[0mc              C   s�   t �  day.ttd t �ad} | t�dd� at�  W nH t	j
jk
rh   t�  ttd � t�  Y n tk
r�   t�  Y nX d S )Nzhttps://lagu123.mobi/zJudul lagu atau Nama artis : zsearch.html?q=� �+�enter)�banner�mainurl�input�lg�lx�src�replace�query�getlink1�requests�
exceptions�ConnectionError�err�main�KeyboardInterrupt�menu)�q� r   �<script>r   G   s    

r   c              C   s  t �  g ag at�tt �} t| jd�}xN|j	ddd�D ]<}|�
d�}t�|�d�� |j
ddd�}t�|�d	�� q8W d
}ttd t��  � x.tD ]&}|d7 }tt|dt |d d� � q�W y
t�  W nJ tjjk
r�   t�  ttd � t�  Y n tk
�r   t�  Y nX d S )Nzhtml.parser�divzdetail-thumb)�class_�a�hrefZimgZicon�altr   zHasil untuk �   z. �(   r   )r	   �link1�titler   �getr
   r   �bs�text�find_all�find�append�printr   r   �upper�lw�getlinkdownloadr   r   r   r   r   r   r   )�r�b�ir   r    �nr   r   r   r   X   s.    



r   c              C   s�  g } xt d�D ]}| �|� qW ttd t �ax(tdksFtt�| krXttd t �aq2W tt�at�t	t
td   �}t|jd�}|jddd	�}|�d
�}t�dt|��a|�d�}t	|�d� ay
t�  W nJ tjjk
r�   t�  ttd � t�  Y n tk
�r   t�  Y nX t�  ttd � td� ttd t ttd   � ttd t td  � ttd t d t � ttd t �}|dk�r�y
t �  W n tk
�r�   t�  Y nX nt�  d S )N�   z
pilih nomor : � zpilih nomor : r!   zhtml.parserr   zbh-info)r   r0   z\Duration: (.*?)\ �sourcer   r   zSukses gan..�2__________________________________________________zJudul Lagu : zDurasi     : r   zFolder     : zResults/z
Langsung puter lagunya? y/n: �y)!�ranger*   r   r   r   r   �intr   r%   r
   r#   r&   r'   r)   r(   �reZfindall�str�d2�linkdownload�trdr   r   r   r   r   r   r	   r+   r-   r$   �kontol�play)�zr1   r/   r0   �cZd1r5   �pyr   r   r   r.   u   sF    





r.   c              C   s  t jtddid�} ttd  �dd�at�dd�at�d	d�at�d
d�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�at�dd�atd atdt d��| j	� d S )Nz
User-AgentzJDalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD)Zheadersr!   r   �_�"r4   �(�)�>�<�/�.�|�&�$�%�=�,�@�#�'�*z.mp3zResults/�wb)
r   r%   r=   r$   r   r   r?   �open�writeZcontent)Zreqr   r   r   �
downloader�   s*    rY   c              C   sD   dddg} x4| D ],}t td | dd�f tj��  td� qW d S )Nz .   z ..  z ... zLagi Downloadr4   )�endg�������?)r+   r   �sys�stdout�flushr   )�kZanr   r   r   �anim�   s
    

 
 r_   c              C   s,   t dtd�} | ��  x| �� r&t�  qW d S )NrY   )�name�target)�TrY   �start�isAliver_   )�tr   r   r   r>   �   s    
r>   c               C   s    t jdt gdt jt jd� d S )Nzmpv Results/T)�shellr\   �stderr)�sp�callr?   ZDEVNULLZSTDOUTr   r   r   r   �ply�   s    rj   c              C   s&  t td � t td t d t d t d t d � t td � td �d	�} t| d �d
 t| d � } tdtd�}|��  |�	� r�d}xjt
d
�D ]^}xXt
d
�D ]L}|| kr�P q�|d7 }t d�tt||tttd �dd� tj��  td� q�W q�W ttd t �}|dk�rt�  nt�  d S )Nz)Musik Player interface by Karjok PangestyzTekan zctrl+c �atauz	 vol up+cz untuk berhentir6   r   �:�<   r!   �player)r`   ra   �����u    {}Durasi > {}{}:{}{} • {}{}  r4   )rZ   zPuter lagi ? y/n: r7   )r+   r-   r   r<   �splitr9   rb   rj   rc   rd   r8   �formatr[   r\   r]   r   r   r   r@   r   )�durasire   �stop�menit�detikZkuntulr   r   r   r@   �   s*    ," 
 
r@   c            .   C   s�   t �d� td�ttttttttttttttttttttttttttttttttttttttttttt�+� ttd � ttd � td� d S )N�clearu�  
            {}:::{}╗{}   :::{}╗{}::{}╗{}   ::{}╗{}
            ::::{}╗{} ::::{}║{}::{}║{}   ::{}║{} 
            ::{}╔{}::::{}╔{}::{}║{}::{}║{}   ::{}║{} 
            ::{}║╚{}::{}╔╝{}::{}║{}::{}║{}   ::{}║╔═╗╦╦╔═{}
            ::{}║ ╚═╝{} ::{}║╚{}::::::{}╔╝╚═╗║╠╩╗
            ╚═╝     ╚═╝ ╚═════╝ ╚═╝╩╩ ╩z)          Download, listen and Enjoy it !r6   �
)rh   ri   r+   rq   �lyr   r-   r   r   r   r   r	   �   s    
`r	   c              C   s�  t �  ttd t d � ttd t d � ttd t d � ttd t d � ttd	 t d
 � ttd t d � ttd t d � ttd t �} | dkr�t�  �n| dk�ry
t�  W n@ tj	j
k
r�   t�  ttd � t�  Y n   t�  Y nX n�| dk�rfy
t�  W nB tj	j
k
�rR   t�  ttd � t�  Y n   t�  Y nX nl| dk�r�y
t�  W n   t�  Y nX nB| dk�r�y
t�  W n   t�  Y nX n| dk�r�t�  nt�  d S )Nz1.z	Cari Laguz2.zCari Lirik Laguz3.zCari Chord Laguz4.zPutar Musikz5.z
Baca Lirikz6.ZTentangz0.ZKeluarz	
Musik # �1�2r   �3�4�5�6)r	   r+   r   r-   r   r   r   �getliriklinkr   r   r   r   r   �getlinkchord�playy�chordlirikmenu�about�exit)Zpir   r   r   r   �   sT    











r   c               C   sP   t �  td�tttttttttttttt�� ttd � ttd � t�  d S )Na�  
{}Nama        : {}Musik
{}Author      : {}Karjok Pangesty
{}Versi       : {}1.0
{}Tanggal     : {}21 Januari 3.12PM
{}Buat Apa?   : {}Fungsi awal Buat download musik.
              Meskipun uda banyak yg buat,
              tapi ini agak beda.
              disini lu nggak cuma
              bisa download musik,
              tapi juga bisa nyari lirik lagu,
              nyari chord lagu trus disimpen,
              dengerin musik yg udah
              didownload pun juga bisa disini.
              intinya beda ea akmj, cobain aja.
{}Terimakasih : {}Allah SWT, Eka Pangesty,
              CRABS, dan kalian yg makek :*
{}NB          : {}Kalo ada error, jan diem-diem bae
              Hubungi gw, https://t.me/om_karjok.r6   r   )r	   r+   rq   r   r-   r   r   r   r   r   r   r�     s    &r�   c               C   s   t d�ttt�� d S )Nz=
                      {}^..^
{}Jaringannya error gan{} (oo)
)r+   rq   �lp�lrr   r   r   r   r   6  s    r   c              C   sz   t �  td�tttt�� ttd t �} | dkrXyt�  t�  W qv   t	�  Y qvX ny
t
�  W n   t	�  Y nX d S )Nz 
{}1. {}Putar
{}2. {}Putar SemuazPilih : rz   )rn   r+   rq   r   r-   r   r   �playmassr�   r   �
playsingle)Zmsjr   r   r   r�   <  s    

r�   c              C   s�   t �  ttd � tdd��} tjdd| d� W d Q R X | ��  tdd��� at	t�dkrztt
d	 � ttd
 � t�  n g }d}xBtD ]:}|d7 }|�|�dd�� td�t|t
|�dd��� q�W ttd � ttd � d S )NzDaftar Lagu
z._�wz
ls ResultsT)rf   r\   r/   r   z8List masih kosong !
Silahkan cari dan download lagu dulur   r!   rw   r4   z
{}{}. {}{}r6   zctrl + c untuk kembali ke menu)r	   r+   r   rW   rh   ri   �close�	readlines�lst�lenr-   r   r   r*   r   rq   )rA   �ttl�nor1   r   r   r   rn   M  s$    
 rn   c              C   s�  g } xt D ]}| �|�dd�� q
W �x�| D �]v}t�  |}td| �}|a|jj}t|��	d�d }t
|�dkr�t
|�d }t|��dd�d d� }nd	| }t�  ttd
 � td�tt|tt|�� ttd � ttd t d t d t d t d � ttd � |atdtd�}|��  |�� r,d}	xptd�D ]d}
x\td�D ]P}|	t
|�k�r`P n8|	d7 }	td�tt|
|tt|�dd� tj��  td� �qJW �q<W q,W d S )Nrw   r4   zResults/rK   r   rm   rl   �   z0:zSedang diputarz'
{}Judul  : {}{}
{}Durasi : {}{}
      z)Musik Player interface by Karjok PangestyzTekan zctrl+c rk   z	 vol up+cz untuk berhentir6   rn   )r`   ra   ro   r!   u    {}Durasi > {}{}:{}{} • {}{}  )rZ   )r�   r*   r   r	   r   r?   �info�lengthr;   rp   r9   r+   r   rq   r-   rb   rj   rc   rd   r8   r[   r\   r]   r   )Ztitlr1   rA   �judulnya�drsrr   �menitan�menittre   rs   rt   ru   r   r   r   r�   h  sD    
, 
 r�   c              C   s�  g } xt D ]}| �|�dd�� q
W tttd t ��}| |d  }|d }td| |  �}| | a|j	j
}t|��d�d }t|�dkr�t|�d }t|��dd	�d d
� }nd| }t�  ttd � td�tt|tt|�� ttd � ttd t d t d t d t d � ttd � tdtd�}|��  |�� �r�d}	xptd�D ]d}
x\td�D ]P}|	t|�k�rvP n8|	d7 }	td�tt|
|tt|�dd� tj��  td� �q`W �qRW td� t�  d S )Nrw   r4   z
Nomor lagu: r!   zResults/rK   r   rm   rl   r�   z0:zSedang diputarz'
{}Judul  : {}{}
{}Durasi : {}{}
      z)Musik Player interface by Karjok PangestyzTekan zctrl+c rk   z	 vol up+qz untuk berhentir6   rn   )r`   ra   ro   u    {}Durasi > {}{}:{}{} • {}{}  )rZ   )r�   r*   r   r9   r   r   r   r   r?   r�   r�   r;   rp   r	   r+   rq   r-   rb   rj   rc   rd   r8   r[   r\   r]   r   rn   )r�   r1   Zslxr�   r�   rr   r�   r�   re   rs   rt   ru   r   r   r   r�   �  sF    
,
 
 r�   c           	   C   s$  g a g } g }t�  ttd t ��dd�}t�d| d �}t|j	d�}xb|j
ddd	�D ]P}|�d
�}|�
d�}x|d D ]}|�|� qzW t �|�d�� | �|j	� qXW d}x4t| |�D ]&\}	}
|d7 }td�t|t|	|
�� q�W tttd t ��atd ay
t�  W n   t�  Y nX d S )NzCari Lirik Lagu: r   r   z)https://search.azlyrics.com/search.php?q=z&w=songs&p=1zhtml.parserZtdztext-left visitedlyr)r   r   r0   r!   r   r   z{}{}. {}{} - {}z
Pilih Nomor : )�linkr	   r   r   r   r   r   r%   r&   r'   r(   r)   r*   �zipr+   rq   r-   r9   �pilih�getlirikr   )�judul�artisr   r/   rA   r1   r   r0   r�   Zju�artr   r   r   r   �  s0    


r   c              C   s,  t �  g } t�tt �}t|jd�}x|�d�D ]}| �|� q0W t	t
| d j � t	t| d j � tt
d t �}| d j}|�dd�}|�dd	�}|d
k�r"yt�d� W n tk
r�   Y nX td| d d�}|�| d j| d j � |��  t	td | d � tt
d � t�  nt�  d S )Nzhtml.parserr   �   r3   zSimpan teks lirik ? y/n: r   rD   rE   r4   r7   ZLirikzLirik/z.txtr�   zTersimpan di Lirik/r   )r	   r   r%   r�   r�   r&   r'   r(   r*   r+   r   r-   r   r   r   �os�mkdir�OSErrorrW   rX   r�   r   )Ztankr/   rA   r1   �sv�jd�lr   r   r   r�   �  s0    

r�   c              C   s:  yt �d� W n tk
r"   Y nX t�  ttd � tdd��} tjdd| d� W d Q R X | �	�  tdd��
� }t|�d	kr�ttd
 � ttd � t�  n g }d	}xB|D ]:}|d7 }|�|�dd�� td�t|t|�dd��� q�W tttd t ��}|d }t�  tjd||  gdd� ttd � t�  d S )N�ChordzDaftar Lirik Lagu
z.__r�   zls LirikT)rf   r\   r/   r   z9List masih kosong !
Silahkan cari dan download lirik dulur   r!   rw   r4   z
{}{}. {}{}zPilih Lirik: z
cat Lirik/)rf   z
enter)r�   r�   r�   r	   r+   r   rW   rh   ri   r�   r�   r�   r-   r   r�   r*   r   rq   r9   r   �	bacalirik)rA   r�   �lirikr�   r1   �plr   r   r   r�   �  s4    
 r�   c        	   	   C   s  t �  g ag ag attd t ��dd�} t�	d|  �}t
|jd�}xn|jddd�D ]\}|jd	d
d�j}|jd	dd�j}t�|�	d�� t�d�|�� �� t�d�|�� �� qTW d}x4ttt�D ]&\}}|d7 }td�t|t||�� q�W tttd t ��atd at�  d S )NzCari Chord Lagu: r   r   z%http://chordarena.com/m/search?query=zhtml.parserr   zrecent-chord__link)r   r   zrecent-chord__item__artistzrecent-chord__item__versionr   r   r!   z{}{}. {}{} - {}zPilih Chord Lagu: )r	   �ur�jdlr�   r   r   r   r   r   r%   r&   r'   r(   r)   r*   �joinrp   r�   r+   rq   r-   r9   r�   �getchord)	Zqrr/   r0   r1   r�   r�   r�   Zarr�   r   r   r   r�     s(    r�   c              C   s  t �  t�dtt  �} t| jd�}|jddd�}td�	t
t tt �� t|j� ttd t �}t
t d tt  }|d	k�ryt�d
� W n tk
r�   Y nX td|�dd� d d�}|�||j � |��  ttd |�dd� d � ttd � t�  nt�  d S )Nzhttp://chordarena.comzhtml.parser�prezsong-content__pre)r   zChord gitar {} - {}zSimpan teks lirik ? y/n: �-r7   r�   zChord/r   rD   z.txtr�   zTersimpan di Chord/r   )r	   r   r%   r�   r�   r&   r'   r)   r+   rq   r�   r�   r   r   r   r�   r�   r�   rW   r   rX   r�   r-   r   r�   )r/   r0   r�   r�   r�   r�   r   r   r   r�   -  s(    

r�   c              C   s:  yt �d� W n tk
r"   Y nX t�  ttd � tdd��} tjdd| d� W d Q R X | �	�  tdd��
� }t|�d	kr�ttd
 � ttd � t�  n g }d	}xB|D ]:}|d7 }|�|�dd�� td�t|t|�dd��� q�W tttd t ��}|d }t�  tjd||  gdd� ttd � t�  d S )Nr�   zDaftar Chord Lagu
z.___r�   zls ChordT)rf   r\   r/   r   z9List masih kosong !
Silahkan cari dan download chord dulur   r!   rw   r4   z
{}{}. {}{}z
Pilih Chord: z
cat Chord/)rf   z
enter)r�   r�   r�   r	   r+   r   rW   rh   ri   r�   r�   r�   r-   r   r�   r*   r   rq   r9   r   �	bacachord)rA   r�   r�   r�   r1   r�   r   r   r   r�   E  s4    
 r�   c           	   C   s�   t �  td�tttttt�� ttd t �} | dkrVy
t�  W q�   t�  Y q�X n.| dkr~y
t	�  W q�   t�  Y q�X nt
�  d S )Nz0
{}1.{} Baca Lirik
{}2.{} Baca Chord
{}0.{} Menuz
Pilih: ry   rz   )r	   r+   rq   r   r-   r   r   r�   r�   r�   r   )Zinpr   r   r   r�   e  s    

r�   �__main__ZResults)1�__doc__r   Zbs4r   r&   Z	threadingr   rb   Zmutagen.mp3r   �
subprocessrh   r:   r[   r�   Ztimer   r   r�   r-   r�   rx   r   r   r   r.   rY   r_   r>   rj   r@   r	   r   r�   r   r�   rn   r�   r�   r   r�   r�   r�   r�   r�   r�   �__name__r�   r�   r   r   r   r   �<module>8   sZ   ).+,! 

)�marshal�exec�loads� r   r   �musik.py�<module>   s   