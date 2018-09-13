import os
import os.path
import struct
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


IMAGE_TYPE = ".png"


def parse(file_path, output):
    # output image name
    root, ext = os.path.splitext(file_path)
    print(root)
    print(ext)
    base_dir, file_name = os.path.split(root)
    print(file_name)
    _, base_name = os.path.split(base_dir)

    output_dir = os.path.join(output, base_name)
    # if output doesn't exit, create.
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    output_image_name = os.path.join(output_dir, "%s%s" % (file_name, IMAGE_TYPE))

    fid = open(file_path, 'rb')   # 'r'は読み込み専用、'b'はバイナリモードで読み込みを表す

    # file signature
    data1_1 = struct.unpack('4s', fid.read(4))
    print("file signature: %s" % data1_1[0])

    # reserved
    data1_2 = struct.unpack('6s', fid.read(6))
    print("reserved: %s" % data1_2)

    # exam date
    data1_3 = struct.unpack('7s', fid.read(7))
    print("exam date: %s" % data1_3)

    # patient name
    data1_4 = struct.unpack('41s', fid.read(41))
    print("patient name: %s" % data1_4)

    # name of examining physician
    data1_5 = struct.unpack('41s', fid.read(41))
    print("name of examining physician: %s" % data1_5)

    # age(years)
    data1_6 = struct.unpack('4s', fid.read(4))
    print("age(years): %s" % data1_6)

    # weight(kg)
    data1_7 = struct.unpack('4s', fid.read(4))
    print("weight(kg): %s" % data1_7)

    # Gender
    data1_8 = struct.unpack('10s', fid.read(10))
    print("gender: %s" % data1_8)

    # Height
    data1_9 = struct.unpack('5s', fid.read(5))
    print("height: %s" % data1_9)

    # Exam time
    data1_10 = struct.unpack('6s', fid.read(6))
    print("exam time: %s" % data1_10)

    # Pacemaker
    data1_11 = struct.unpack('4s', fid.read(4))
    print("pacemaker: %s" % data1_11)

    # Average heart rate
    data1_12 = struct.unpack('4s', fid.read(4))
    print("average hear rate: %s" % data1_12)

    # Systolic pressure
    data1_13 = struct.unpack('4s', fid.read(4))
    print("systolic pressure: %s" % data1_13)

    # diastolic pressure
    data1_14 = struct.unpack('4s', fid.read(4))
    print("diastolic pressure: %s" % data1_14)

    # name of examining pysisian
    data1_15 = struct.unpack('36s', fid.read(36))
    print("name of examining pysisian: %s" % data1_15)

    # Rhythm
    data1_16 = struct.unpack('21s', fid.read(21))
    print("rhythm: %s" % data1_16)

    # P-wave in ms
    data1_17 = struct.unpack('5s', fid.read(5))
    print("P-wave(ms): %s" % data1_17)

    # PR segment in ms
    data1_18 = struct.unpack('5s', fid.read(5))
    print("PR segment(ms): %s" % data1_18)

    # QRS segment in ms
    data1_19 = struct.unpack('5s', fid.read(5))
    print("QRS segment(ms): %s" % data1_19)

    # QT segment in ms
    data1_20 = struct.unpack('5s', fid.read(5))
    print("QT segment(ms): %s" % data1_20)

    # SAP angle in degrees
    data1_21 = struct.unpack('5s', fid.read(5))
    print("SAP angle(degrees): %s" % data1_21)

    # SAQRS angle in degrees
    data1_22 = struct.unpack('5s', fid.read(5))
    print("SAQRS angle(degrees): %s" % data1_22)

    # researved 474
    data1_23 = struct.unpack('474s', fid.read(474))
    print("reserved: %s" % data1_23)

    # sequential register number
    data1_24 = struct.unpack('<I', fid.read(4))
    print("sequential register number: %s" % data1_24)

    # equipment firmware version
    for i in range(2):
        # for example V 2.5 the first is 2 and the second 5)
        data1_25_little = struct.unpack('<c', fid.read(1))

    # sensitivity
    data1_26 = struct.unpack('4s', fid.read(4))
    print("sensitivity: %s" % data1_26)

    # Heading title
    data1_27 = struct.unpack('26s', fid.read(26))
    print("heading title: %s" % data1_27)

    # Elapsed time from the beginning of the continuous recording block
    data1_28 = struct.unpack('12s', fid.read(12))
    print("Elapsed time from the beginning of the continuous recording block: %s" % data1_28)

    # Elapsed time from the beginning of the exam
    data1_29 = struct.unpack('12s', fid.read(12))
    print("Elapsed time from the beginning of the exam: %s" % data1_29)

    # network filter binary
    data1_30 = struct.unpack('c', fid.read(1))
    print("network filter binary: %s" % data1_30)

    # muscle tremor filter binary
    data1_31 = struct.unpack('c', fid.read(1))
    print("muscle tremor filter binary: %s" % data1_31)

    # baseline or hich pass filter binary
    data1_32 = struct.unpack('c', fid.read(1))
    print("baseline or high pass fliter binary: %s" % data1_32)

    # name of derivation 1 ~ 12
    derivation_names = []
    for i in range(12):
        data1_33_44 = struct.unpack('4s', fid.read(4))
        derivation_names.append(data1_33_44)

    # age in months
    data1_45 = struct.unpack('4s', fid.read(4))
    print("age(months): %s" % data1_45)

    # weight in grams
    data1_46 = struct.unpack('4s', fid.read(4))
    print("weight(grams): %s" % data1_46)

    # reserved
    data1_47 = struct.unpack('24s', fid.read(24))
    print("reserved: %s" % data1_47)

    # turn off lead 1 ~ 12 in single window display
    for i in range(12):
        data1_48_59 = struct.unpack('b', fid.read(1))
        print("turn off lead %d: %s" % (i + 1, data1_48_59))

    # Pace maker type
    data1_60 = struct.unpack('31s', fid.read(31))
    print("pace maker type: %s" % data1_60)

    # date of implantation of the pacemaker
    data1_61 = struct.unpack('7s', fid.read(7))
    print("date of implantation of the pacemaker: %s" % data1_61)

    # complementary patient identification field 1 ~ 3
    for i in range(3):
        data1_62_64 = struct.unpack('17s', fid.read(17))
        print("complementary patient identification %d: %s" % (i + 1, data1_62_64))

    # reserved
    data1_65 = struct.unpack('7s', fid.read(7))
    print("reserved: %s" % data1_65)

    # unique identifier of the exam
    data1_66 = struct.unpack('21s', fid.read(21))
    print("unique identifier of the exam: %s" % data1_66)

    # rg number
    data1_67 = struct.unpack('21s', fid.read(21))
    print("rg number: %s" % data1_67)

    # cpf number
    data1_68 = struct.unpack('21s', fid.read(21))
    print("cpf number: %s" % data1_68)

    # patient's last name
    data1_69 = struct.unpack('26s', fid.read(26))
    print("patient's last name: %s" % data1_69)

    # date of birth
    data1_70 = struct.unpack('11s', fid.read(11))
    print("date of birth: %s" % data1_70)

    # civil status
    data1_71 = struct.unpack('2s', fid.read(2))
    print("civil status: %s" % data1_71)

    # occupation
    data1_72 = struct.unpack('21s', fid.read(21))
    print("occupation: %s" % data1_72)

    # address
    data1_73 = struct.unpack('41s', fid.read(41))
    print("address: %s" % data1_73)

    # complement
    data1_74 = struct.unpack('21s', fid.read(21))
    print("complement: %s" % data1_74)

    # neighborhood
    data1_75 = struct.unpack('31s', fid.read(31))
    print("neighborhood: %s" % data1_75)

    # city
    data1_76 = struct.unpack('31s', fid.read(31))
    print("city: %s" % data1_76)

    # federation unit
    data1_77 = struct.unpack('3s', fid.read(3))
    print("federation unit: %s" % data1_77)

    # cep
    data1_78 = struct.unpack('10s', fid.read(10))
    print("cep: %s" % data1_78)

    # home telephone
    data1_79 = struct.unpack('15s', fid.read(15))
    print("home telephone: %s" % data1_79)

    # business phone
    data1_80 = struct.unpack('15s', fid.read(15))
    print("business phone: %s" % data1_80)

    # email
    data1_81 = struct.unpack('41s', fid.read(41))
    print("email: %s" % data1_81)

    # data added
    data1_82 = struct.unpack('11s', fid.read(11))
    print("data added: %s" % data1_82)

    # exam number
    data1_83 = struct.unpack('11s', fid.read(11))
    print("exam number: %s" % data1_83)

    # clinical data
    data1_84 = struct.unpack('280s', fid.read(280))
    print("clinical data: %s" % data1_84)

    # drugs in use
    data1_85 = struct.unpack('189s', fid.read(189))
    print("drugs in use: %s" % data1_85)

    # responsible CRM
    data1_86 = struct.unpack('21s', fid.read(21))
    print("responsible CRM: %s" % data1_86)

    # reserved
    data1_87 = struct.unpack('b', fid.read(1))
    print("reserved: %s" % data1_87)

    # date and time of signature of the award
    data1_88 = struct.unpack('6s', fid.read(6))
    print("date and time of signature of the award: %s" % data1_88)

    # equipment serial number
    data1_89 = struct.unpack('10s', fid.read(10))
    print("equipment serial number: %s" % data1_89)

    # samples of derivation 1 ~ 12
    # 26880 bytes being 13440 samples of 16 bits;
    # 1_90 ~ 1_102
    derivation = []
    for n in range(12):
        derivation_n = []
        for i in range(13440):
            data1_90 = struct.unpack('<h', fid.read(2))
            derivation_n.append(data1_90[0])
        derivation.append(derivation_n)

    # create fugure of samples of derivation 1 ~ 12
    fig1 = plt.figure()
    for n in range(12):
        ax = fig1.add_subplot(12, 1, n + 1)
        ax.plot(derivation[n])
        if n is not 11:
            plt.setp(ax.get_xticklabels(), visible=False)
        ax.yaxis.tick_right()
        ax.set_ylabel(derivation_names[n][0].decode('utf-8').strip('\r\n\0'))

    # TODO image saving
    #plt.show()
    plt.savefig(output_image_name, bbox_inches='tight')

    # State of the electrodes in each sample
    electrodes = []
    for i in range(13440):
        status = []
        data1_102 = struct.unpack('<h', fid.read(2))
        status.append(data1_102[0] & 0b0000000000000001)
        status.append(data1_102[0] & 0b0000000000000010)
        status.append(data1_102[0] & 0b0000000000000100)
        status.append(data1_102[0] & 0b0000000000001000)
        status.append(data1_102[0] & 0b0000000000010000)
        status.append(data1_102[0] & 0b0000000000100000)
        status.append(data1_102[0] & 0b0000000001000000)
        status.append(data1_102[0] & 0b0000000010000000)
        status.append(data1_102[0] & 0b0000000100000000)
        status.append(data1_102[0] & 0b0000001000000000)
        electrodes.append(status)
