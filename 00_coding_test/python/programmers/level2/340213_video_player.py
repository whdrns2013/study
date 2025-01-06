def solution(video_len, pos, op_start, op_end, commands):
    def convert_to_sec(time):
        return 60*int(time.split(':')[0]) + int(time.split(':')[1])
    video_len = convert_to_sec(video_len)
    pos = convert_to_sec(pos)
    op_start = convert_to_sec(op_start)
    op_end = convert_to_sec(op_end)
    for command in commands:
        if (pos <= op_end) & (pos >= op_start):
            pos = op_end
        if command == 'next':
            pos = min(pos + 10, video_len)
        elif command == 'prev':
            pos = max(pos - 10, 0)
        if (pos <= op_end) & (pos >= op_start):
            pos = op_end
    answer = str(pos//60).zfill(2) + ':' + str(pos%60).zfill(2)
    return answer