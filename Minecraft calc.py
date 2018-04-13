from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x, y, z = mc.player.getPos()
grass = 2
stone = 1

global firstNumber
global secondNumber
global currentNumber
global operator
firstNumber = 0
secondNumber = 0
currentNumber = 0
operator = ""
def get_blocks(x, y, z):
    block1 = mc.getBlock(x+2, y-1, z-2)
    block2 = mc.getBlock(x+2, y-1, z-1)
    block3 = mc.getBlock(x+2, y-1, z)
    block4 = mc.getBlock(x+2, y-1, z+1)
    block5 = mc.getBlock(x+2, y-1, z+2)
    block6 = mc.getBlock(x+1, y-1, z-2)
    block7 = mc.getBlock(x+1, y-1, z-1)
    block8 = mc.getBlock(x+1, y-1, z)
    block9 = mc.getBlock(x+1, y-1, z+1)
    block10 = mc.getBlock(x+1, y-1, z+2)
    block11 = mc.getBlock(x, y-1, z-2)
    block12 = mc.getBlock(x, y-1, z-1)
    block13 = mc.getBlock(x, y-1, z)
    block14 = mc.getBlock(x, y-1, z+1)
    block15 = mc.getBlock(x, y-1, z+2)
    block16 = mc.getBlock(x-1, y-1, z-2)
    block17 = mc.getBlock(x-1, y-1, z-1)
    block18 = mc.getBlock(x-1, y-1, z)
    block19 = mc.getBlock(x-1, y-1, z+1)
    block20 = mc.getBlock(x-1, y-1, z+2)
    block21 = mc.getBlock(x-2, y-1, z-2)
    block22 = mc.getBlock(x-2, y-1, z-1)
    block23 = mc.getBlock(x-2, y-1, z)
    block24 = mc.getBlock(x-2, y-1, z+1)
    block25 = mc.getBlock(x-2, y-1, z+2)
    return([block1,block2,block3,block4,block5,\
            block6,block7,block8,block9,block10,\
            block11,block12,block13,block14,block15,\
            block16,block17,block18,block19,block20,\
            block21,block22,block23,block24,block25])

def is_0(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] != grass and \
           blocks[7] == grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] != grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_1(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] == grass and \
           blocks[2] != grass and \
           blocks[3] == grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] != grass and \
           blocks[7] != grass and \
           blocks[8] == grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] == grass and \
           blocks[13] == grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] != grass and \
           blocks[18] == grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_2(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] == grass and \
           blocks[7] == grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] != grass and \
           blocks[17] == grass and \
           blocks[18] == grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_3(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] == grass and \
           blocks[7] == grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_4(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] == grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] != grass and \
           blocks[7] == grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] == grass and \
           blocks[22] == grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_5(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] != grass and \
           blocks[7] == grass and \
           blocks[8] == grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_6(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] != grass and \
           blocks[7] == grass and \
           blocks[8] == grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] != grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_7(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] == grass and \
           blocks[7] == grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] == grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] == grass and \
           blocks[22] == grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_8(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] == grass and \
           blocks[4] == grass and \
           blocks[5] != grass and \
           blocks[6] == grass and \
           blocks[7] == grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] != grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] != grass and \
           blocks[16] == grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] == grass and \
           blocks[24] == grass
def is_9(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] != grass and \
           blocks[2] != grass and \
           blocks[3] != grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] != grass and \
           blocks[7] == grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] == grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] != grass and \
           blocks[22] != grass and \
           blocks[23] != grass and \
           blocks[24] == grass
def is_plus(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] == grass and \
           blocks[2] == grass and \
           blocks[3] == grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] == grass and \
           blocks[7] != grass and \
           blocks[8] == grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] != grass and \
           blocks[18] == grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] == grass and \
           blocks[22] == grass and \
           blocks[23] == grass and \
           blocks[24] == grass
def is_minus(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] == grass and \
           blocks[2] == grass and \
           blocks[3] == grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] == grass and \
           blocks[7] == grass and \
           blocks[8] == grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] != grass and \
           blocks[13] != grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] == grass and \
           blocks[17] == grass and \
           blocks[18] == grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] == grass and \
           blocks[22] == grass and \
           blocks[23] == grass and \
           blocks[24] == grass
def is_equals(blocks):
    return blocks[12] == stone and \
           blocks[0] == grass and \
           blocks[1] == grass and \
           blocks[2] == grass and \
           blocks[3] == grass and \
           blocks[4] == grass and \
           blocks[5] == grass and \
           blocks[6] != grass and \
           blocks[7] != grass and \
           blocks[8] != grass and \
           blocks[9] == grass and \
           blocks[10] == grass and \
           blocks[11] == grass and \
           blocks[13] == grass and \
           blocks[14] == grass and \
           blocks[15] == grass and \
           blocks[16] != grass and \
           blocks[17] != grass and \
           blocks[18] != grass and \
           blocks[19] == grass and \
           blocks[20] == grass and \
           blocks[21] == grass and \
           blocks[22] == grass and \
           blocks[23] == grass and \
           blocks[24] == grass
           
def get_key(x, y, z):
    blocks = get_blocks(x, y, z)
    if is_0(blocks):
        return(0)
    elif is_1(blocks):
        return(1)
    elif is_2(blocks):
        return(2)
    elif is_3(blocks):
        return(3)
    elif is_4(blocks):
        return(4)
    elif is_5(blocks):
        return(5)
    elif is_6(blocks):
        return(6)
    elif is_7(blocks):
        return(7)
    elif is_8(blocks):
        return(8)
    elif is_9(blocks):
        return(9)
    elif is_plus(blocks):
        return("+")
    elif is_minus(blocks):
        return("-")
    elif is_equals(blocks):
        return("=")
    else:
        return(-1)
def print_key(x, y, z):
    key = get_key(x, y, z)
    mc.postToChat(key)
    
def updateCurrentNumber(key):
    global operator
    global firstNumber
    global secondNumber
    if operator == "":
        firstNumber = key
    else:
        secondNumber = key
        
def calculate(first, op, second):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    else:
        return(first)
        
        
def run(x, y, z):
    global firstNumber
    global secondNumber
    global operator
    key = get_key(x, y, z)
    if key == "=":
        result = calculate(firstNumber, operator, secondNumber)
        mc.postToChat("RESULT:")
        mc.postToChat(result)
        firstNumber = 0
        secondNumber = 0
        operator = ""
    elif key == "+" or key == "-":
        mc.postToChat(key)
        operator = key
    elif key < 10 and key > -1:
        mc.postToChat(key)
        updateCurrentNumber(key)
    
while True:
    sleep(0.5)
    x, y, z = mc.player.getPos()
    run(x, y, z)
