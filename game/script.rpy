# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# Deklarasikan karakter yang digunakan di game.
define ak = Character("Asep Kuda", color="#000000")
define a = Character('Aria', color="#967509")
define q = Character('Quantumia', color="#250a5f")

image giza = Movie(play="pyramid480.webm", pos=(525,200), anchor=(0,0))

# Game dimulai disini.
label start:
    
    # debug

    # scene bg cosmos with dissolve
    
    # show asep kid at topleft with dissolve

    # ak "{cps=10}Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/cps}"

    # play music "jungle.opus"

    # play sound "baba booey.mp3"   

    # ak "baba booey"

    # stop sound

    play music bglethal

    scene black with fade

    "Di sebuah sekolah biasa, Aria, seorang siswi yang penuh semangat untuk belajar, baru saja tiba di laboratorium Profesora Quantumia, ilmuwan eksentrik yang telah lama dikenalnya."

    play sound walk loop

    "Begitu Aria memasuki lab, Profesora Quantumia langsung mengajaknya untuk sebuah petualangan yang menakjubkan."

    stop sound

    play sound dooropen

    scene bg cosmos with dissolve

    show mry_goldsect_happylaugh at left

    a "Hai Profesor Quantumia!"

    show lxc_neutral at right

    q "Hei Aria! Selamat datang di laboratoriumku. Kebetulan sekali kamu datang kesini."

    show mry_goldsect_surprised at left

    a "Emang kenapa profesor?"

    q "Nih, aku punya barang keren nih. Ini namanya \"Teleporter\"."

    q "Ini adalah alat yang bisa membuat kita berpindah tempat ke mana saja tanpa harus repot."

    a "Wow, suara keren banget! emang cara kerjanya gimana sih?"

    q "Jadi begini, Teleporter ini pakai baru yang udah aku ciptain."

    q "Kamu tinggal set koordinatnya, kita bisa langsung pindah ke tempat yang kita mau."

    q "Nah, ideku sekarang, bagaimana kalau kita bareng-bareng nyobain ini?"

    a "Serius? Itu keren banget, Profesor. Emang kita mau pergi kemana dulu?"

    q "Mari kita coba mesin ini dengan pergi ke mesir!"

    
    menu:
        
        "Kenapa harus ke mesir prof?":
            jump choice1_answer
        "sepertinya menarik.....":        
            jump choice1_answer

    label choice1_answer:
        
        q "Mesir memiliki banyak keunikan, dari sungai nil, sejarah dan peninggalan sejarahnya seperti piramida." 

        jump choice1_done

    label choice1_done:

        a "kalo begitu kita akan pergi kapan prof?"

        q "kita akan pergi sekarang !!"

        a "APAA SEKARANG!!!"

    

    "Bersama-sama, Aria dan Profesora Quantumia memasuki teleporter dan memulai mesinnya."

    play sound teleport loop

    "Lalu memasukan koordinat piramid giza di mesir. Tiba2 profesor menyalakan mesin dan memindahkan mereka ke mesir tepatnya didekat piramida."

    scene black with fade

    scene bg dune with dissolve

    stop sound

    play music egypt

    show mry_goldsect_neutral at left

    show lxc_neutral at right    


    q "ALAT KU BERHASIL!!!"

    a "setidaknya kita mendarat dengan mulus."

    a "uwu, pemandangannya sungguh indah sekali."

    q "kita tidak hanya datang ke sini untuk menikmati pemandangan. Ada sesuatu yang menarik perhatian saya. Lihatlah ke arah matahari terbenam di sana."

    a "apakah itu piramida giza?"

    show giza behind q

    q "benar itu, Piramida Giza adalah salah satu keajaiban dunia kuno yang paling terkenal."

    q "Dalam sejarah Ini dibangun sekitar tahun 2580-2560 SM untuk Pharaoh Khufu. Piramida ini memiliki tinggi lebih dari 138 meter dan sebelumnya lebih tinggi lagi dengan penutup piramida yang hilang."    

    q "selanjutnya kitanya kita pergi ke jepang"

    a "JAPAN !!!"

    q "benar! Kita akan pergi ke kuil yang ada di kyoto jepang."

    a "gass!!"

    "Bersama-sama, Aria dan Profesora Quantumia memasuki teleporter dan memulai mesinnya, lalu memasukan koordinat kuil kyoto di jepang."

    play sound teleport loop

    scene black with dissolve

    "To be continued{cps=5}..........{/cps}"
    

    # play sound teleport

    # choice example
    # menu:

    #     "Asep kuda ganteng":
    #         jump choice1_yes
    #     "Asep kuda jelek":
    #         jump choice1_no
    #     "Trick question! Tou are neither!":
    #         jump choice1_neutral

    # label choice1_yes:

    #     show asep kid at center

    #     ak "i am. Now bend over."

    #     jump choice1_done

    # label choice1_no:

    #     show asep kid at center    

    #     ak "You have incurred my wrath. Die."

    #     jump choice1_done

    # label choice1_neutral:

    #     # $ asep_kid_flag = true

    #     show asep kid at center

    #     ak "You passed the test"

    #     jump choice1_done

    # label choice1_done:

    # ak "back at start we are..."    

    # ak "{cps=3} or are we...??!!!! {/cps}"

    return
