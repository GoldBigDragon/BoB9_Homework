rule iconAndIconGroup {
    meta:
        author = "GoldBigDragon"
        type = "Malware"
        filetype = "Win32 EXE"
        version = "1.0"
        date = "2021-01-21"
        description = "Rule to detect various malware"

    strings:
        $iconGroup = {0000010008003030000001000800A80E00000?002020000001000800A8080000}
        $icon = {EFEFEFEFEF6B6BEF6D6D6D6DEFEF6DEFEF6D6DEF6D56EFEFEFEFEFEFEF6B746B}

    condition:
        1 of them
}