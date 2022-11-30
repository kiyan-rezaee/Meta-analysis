# import struct


def shortcut(fname, name='mehrshad', form='.pdf'):
    if name == 'mehrshad':
        path = r"C:\Documents\Mehrshad\User Intent Modeling"
    return path + '\\' + str(fname) + form


# def shortcut(fname, path='m.lnk', form='.pdf'):
#     target = ''
#     with open(path, 'rb') as stream:
#         content = stream.read()
#         lflags = struct.unpack('I', content[0x14:0x18])[0]
#         position = 0x18
#         if (lflags & 0x01) == 1:
#             position = struct.unpack('H', content[0x4C:0x4E])[0] + 0x4E
#         last_pos = position
#         position += 0x04
#         length = struct.unpack('I', content[last_pos:position])[0]
#         position += 0x0C
#         lbpos = struct.unpack('I', content[position:position + 0x04])[0]
#         position = last_pos + lbpos
#         size = (length + last_pos) - position - 0x02
#         temp = struct.unpack('c' * size, content[position:position + size])
#         target = ''.join([chr(ord(a)) for a in temp])
#     return target + '\\' + str(fname) + form
