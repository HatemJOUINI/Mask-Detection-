import os
import random
import struct
from Crypto.Cipher import AES
import time
import mysql.connector
from mysql.connector import Error


class Cryp_Decry():

    def __init__(self):
        self.key = b"Covid2020Tunisia"
        self.iv = b'0123456789abcdef'

    def encrypt_file(self, in_filename, chunksize=64*1024):
        """ Encrypts a file using AES (CBC mode) with the
            given key.

            key:
                The encryption key - a string that must be
                either 16, 24 or 32 bytes long. Longer keys
                are more secure.

            in_filename:
                Name of the input file

            out_filename:
                If None, '<in_filename>.enc' will be used.

            chunksize:
                Sets the size of the chunk which the function
                uses to read and encrypt the file. Larger chunk
                sizes can be faster for some files and machines.
                chunksize must be divisible by 16.
        """

        out_filename = in_filename + '.enc'
        encryptor = AES.new(self.key, AES.MODE_CBC, self.iv)
        filesize = os.path.getsize(in_filename)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(self.iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    text = encryptor.encrypt(chunk)

                    outfile.write(text)

    def decrypt_file(self, in_filename, out_filename="test.png", chunksize=24*1024):
        """ Decrypts a file using AES (CBC mode) with the
            given key. Parameters are similar to encrypt_file,
            with one difference: out_filename, if not supplied
            will be in_filename without its last extension
            (i.e. if in_filename is 'aaa.zip.enc' then
            out_filename will be 'aaa.zip')
        """
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0]

        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack(
                '<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, self.iv)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(origsize)

    def folder_crypting(self, path_folder):
        try:

            date_string = time.strftime("%Y-%m-%d-%H:%M")
            connection = mysql.connector.connect(host='localhost',
                                                 database='Authority',
                                                 user='root',
                                                 password='covid19')

            for root, dirs, files in os.walk(path_folder):
                for i in files:
                    if i[-1] == 'g':
                        f = open("id_ref.txt", "r")
                        Id_F = f.read()

                        Id_Ff = int(Id_F)

                        self.encrypt_file(path_folder+i)
                        os.remove(path_folder+i)

                        if connection.is_connected():
                            db_Info = connection.get_server_info()
                            print("Connected to MySQL Server version ", db_Info)
                            cursor = connection.cursor()
                            cursor.execute("INSERT INTO Face_Detec(Id_F,Description,Path_Img,time)VALUES("+"\'"+str(
                                Id_Ff)+"\'"+",\'"+str(path_folder)+"\',\'"+str(i)+".enc\'"+",\'"+date_string+"\');")
                            connection.commit()
                            Id_Ff += 1
                            f = open("id_ref.txt", "w")
                            f.write(str(Id_Ff))
                            f.close()
                        else:
                            print("You are not connected to your DATABASE ")
        except:
            print("Please active MySQL service on your computer !!")

    def data_base_decrypt(self, path, id):

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Authority',
                                                 user='root',
                                                 password='covid19')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(
                    "select Path_Img , time from Face_Detec where Id_f like "+id+" ;")
                result = cursor.fetchone()
                self.decrypt_file(path+result[0], result[0])
                f = open("path_img_decrypt.txt", "w")
                f.write(result[0])
                f.close()
            else:
                print("Something went wrong !")
        except:
            print("Please active MySQL service on your computer !!")
