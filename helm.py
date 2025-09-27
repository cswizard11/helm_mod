import mcpi.minecraft as minecraft
import mcpi.block as block
import time

#set up to let the program talk to Minecraft
mc = minecraft.Minecraft.create()
position = mc.player.getPos()
mc.camera.setNormal()
compare = mc.getBlock(position.x, position.y - 1, position.z)
startBlock = [position.x, position.y - 1, position.z, compare]

findBlocks = [startBlock]
shipBlocks = []

#find all the blocks that are part of the ship
while findBlocks != []:
    for i in findBlocks:
        compare = mc.getBlock(i[0], i[1], i[2])
        if not(compare == block.AIR.id or [i[0], i[1], i[2], compare] in shipBlocks):
            addition = [i[0], i[1], i[2], compare]
            shipBlocks.append(addition)
            findBlocks.append(addition)

        compare = mc.getBlock(i[0], i[1] - 1, i[2])
        if not(compare == block.AIR.id or [i[0], i[1] - 1, i[2], compare] in shipBlocks):
            addition = [i[0], i[1] - 1, i[2], compare]
            shipBlocks.append(addition)
            findBlocks.append(addition)

        compare = mc.getBlock(i[0], i[1] + 1, i[2])
        if not(compare == block.AIR.id or [i[0], i[1] + 1, i[2], compare] in shipBlocks):
            addition = [i[0], i[1] + 1, i[2], compare]
            shipBlocks.append(addition)
            findBlocks.append(addition)

        compare = mc.getBlock(i[0], i[1], i[2] - 1)
        if not(compare == block.AIR.id or [i[0], i[1], i[2] - 1, compare] in shipBlocks):
            addition = [i[0], i[1], i[2] - 1, compare]
            shipBlocks.append(addition)
            findBlocks.append(addition)

        compare = mc.getBlock(i[0], i[1], i[2] + 1)
        if not(compare == block.AIR.id or [i[0], i[1], i[2] + 1, compare] in shipBlocks):
            addition = [i[0], i[1], i[2] + 1, compare]
            shipBlocks.append(addition)
            findBlocks.append(addition)

        compare = mc.getBlock(i[0] - 1, i[1], i[2])
        if not(compare == block.AIR.id or [i[0] - 1, i[1], i[2], compare] in shipBlocks):
            addition = [i[0] - 1, i[1], i[2], compare]
            shipBlocks.append(addition)
            findBlocks.append(addition)

        compare = mc.getBlock(i[0] + 1, i[1], i[2])
        if not(compare == block.AIR.id or [i[0] + 1, i[1], i[2], compare] in shipBlocks):
            addition = [i[0] + 1, i[1], i[2], compare]
            shipBlocks.append(addition)
            findBlocks.append(addition)
            
        findBlocks.remove(i)
        print(len(shipBlocks))
        
for i in shipBlocks:
    compare = mc.getBlock(i[0] + 1, i[1], i[2])
    if compare == block.AIR.id:
        i.append("north")
    else:
        i.append("nothing")
        
    compare = mc.getBlock(i[0] - 1, i[1], i[2])
    if compare == block.AIR.id:
        i.append("south")
    else:
        i.append("nothing")

    compare = mc.getBlock(i[0], i[1], i[2] + 1)
    if compare == block.AIR.id:
        i.append("east")
    else:
        i.append("nothing")

    compare = mc.getBlock(i[0], i[1], i[2] - 1)
    if compare == block.AIR.id:
        i.append("west")
    else:
        i.append("nothing")

    compare = mc.getBlock(i[0], i[1] + 1, i[2])
    if compare == block.AIR.id:
        i.append("above")
    else:
        i.append("nothing")

    compare = mc.getBlock(i[0], i[1] - 1, i[2])
    if compare == block.AIR.id:
        i.append("below")
    else:
        i.append("nothing")
    

print("")
mc.postToChat(len(shipBlocks))
mc.postToChat("Move Forward")
mc.player.setPos(position.x, position.y, position.z)

#find what direction the player is facing
forward = "nothing"
while forward == "nothing":
    moved = mc.player.getPos()
    
    if moved.x > position.x:
        forward = "north"
        exit_helm = "south"
        right = "east"
        left = "west"

    if moved.x < position.x:
        forward = "south"
        exit_helm = "north"
        right = "west"
        left = "east"

    if moved.z > position.z:
        forward = "east"
        exit_helm = "west"
        right = "south"
        left = "north"
        
    if moved.z < position.z:
        forward = "west"
        exit_helm = "east"
        right = "north"
        left = "south"
    
    if moved.x > position.x and moved.z > position.z:
        if (moved.x - position.x) > (moved.z - position.z):
            forward = "north"
            exit_helm = "south"
            right = "east"
            left = "west"
        if (moved.x - position.x) < (moved.z - position.z):
            forward = "east"
            exit_helm = "west"
            right = "south"
            left = "north"
            
    if moved.x > position.x and moved.z < position.z:
        if (moved.x - position.x) > (position.z - moved.z):
            forward = "north"
            exit_helm = "south"
            right = "east"
            left = "west"
        if (moved.x - position.x) < (position.z - moved.z):
            forward = "west"
            exit_helm = "east"
            right = "north"
            left = "south"
        
    if moved.x < position.x and moved.z > position.z:
        if (position.x - moved.x) > (moved.z - position.z):
            forward = "south"
            exit_helm = "north"
            right = "west"
            left = "east"
        if (position.x - moved.x) < (moved.z - position.z):
            forward = "east"
            exit_helm = "west"
            right = "south"
            left = "north"
            
    if moved.x < position.x and moved.z < position.z:
        if (position.x - moved.x) > (position.z - moved.z):
            forward = "south"
            exit_helm = "north"
            right = "west"
            left = "east"
        if (position.x - moved.x) < (position.z - moved.z):
            forward = "west"
            exit_helm = "east"
            right = "north"
            left = "south"
        
mc.postToChat(forward)
time.sleep(0.1)
mc.player.setPos(position.x, position.y, position.z)

direction = "none"

while direction != exit_helm:
    #find what player is moving
    time.sleep(0.5)
    moved = mc.player.getPos()
    direction = "none"
    if moved.x > position.x:
        direction = "north"

    if moved.x < position.x:
        direction = "south"

    if moved.z > position.z:
        direction = "east"
        
    if moved.z < position.z:
        direction = "west"
    
    if moved.x > position.x and moved.z > position.z:
        if (moved.x - position.x) > (moved.z - position.z):
            direction = "north"
        if (moved.x - position.x) < (moved.z - position.z):
            direction = "east"
            
    if moved.x > position.x and moved.z < position.z:
        if (moved.x - position.x) > (position.z - moved.z):
            direction = "north"
        if (moved.x - position.x) < (position.z - moved.z):
            direction = "west"
        
    if moved.x < position.x and moved.z > position.z:
        if (position.x - moved.x) > (moved.z - position.z):
            direction = "south"
        if (position.x - moved.x) < (moved.z - position.z):
            direction = "east"
            
    if moved.x < position.x and moved.z < position.z:
        if (position.x - moved.x) > (position.z - moved.z):
            direction = "south"
        if (position.x - moved.x) < (position.z - moved.z):
            direction = "west"

    if moved.y > position.y:
        direction = "up"

    if moved.y < position.y:
        direction = "down"

    #move the ship forward
    if direction == forward:
        if  forward == "north":
            for i in shipBlocks:
                i[0] += 1
                mc.setBlock(i[0], i[1], i[2], i[3])
                if i[5] == "south":
                    mc.setBlock(i[0] - 1, i[1], i[2], block.AIR.id)
            position.x +=1

        if  forward == "south":
            for i in shipBlocks:
                i[0] -= 1
                mc.setBlock(i[0], i[1], i[2], i[3])
                if i[4] == "north":
                    mc.setBlock(i[0] + 1, i[1], i[2], block.AIR.id)
            position.x -=1

        if  forward == "east":
            for i in shipBlocks:
                i[2] += 1
                mc.setBlock(i[0], i[1], i[2], i[3])
                if i[7] == "west":
                    mc.setBlock(i[0], i[1], i[2] - 1, block.AIR.id)
            position.z +=1

        if  forward == "west":
            for i in shipBlocks:
                i[2] -= 1
                mc.setBlock(i[0], i[1], i[2], i[3])
                if i[6] == "east":
                    mc.setBlock(i[0], i[1], i[2] + 1, block.AIR.id)
            position.z -= 1

    #move the ship right
    if direction == right:
       if right == "west":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                startX = i[0]
                startZ = i[2]

                
                i[0] = -(startZ - position.z) + position.x
                i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[4] == "north":
                    i[6] = "east"

                elif i[6] == "east":
                    i[5] = "south"

                elif i[5] == "south":
                    i[7] = "west"

                elif i[7] == "west":
                    i[4] = "north"

                else:
                    None
   
            forward = "west"
            exit_helm = "east"
            right = "north"
            left = "south"

       elif right == "east":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                startX = i[0]
                startZ = i[2]

                i[0] = -(startZ - position.z) + position.x
                i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[5] == "south":
                    i[7] = "west"

                elif i[7] == "west":
                    i[4] = "north"

                elif i[4] == "north":
                    i[6] = "east"

                elif i[6] == "east":
                    i[5] = "south"

                else:
                    None
    
            forward = "east"
            exit_helm = "west"
            right = "south"
            left = "north"

       elif right == "south":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                startX = i[0]
                startZ = i[2]

                i[0] = -(startZ - position.z) + position.x
                i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[7] == "west":
                    i[4] = "north"

                elif i[4] == "north":
                    i[6] = "east"

                elif i[6] == "east":
                    i[5] = "south"

                elif i[5] == "south":
                    i[7] = "west"

                else:
                    None

            forward = "south"
            exit_helm = "north"
            right = "west"
            left = "east"

       elif right == "north":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                startX = i[0]
                startZ = i[2]

                i[0] = -(startZ - position.z) + position.x
                i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[6] == "east":
                    i[5] = "south"

                elif i[5] == "south":
                    i[7] = "west"

                elif i[7] == "west":
                    i[4] = "north"

                elif i[4] == "north":
                    i[6] = "east"

                else:
                    None
    
            forward = "north"
            exit_helm = "south"
            right = "east"
            left = "west"

    #move the ship left
    if direction == left:
        if left == "north":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                for j in range(3):
                    startX = i[0]
                    startZ = i[2]

                    i[0] = -(startZ - position.z) + position.x
                    i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[7] == "west":
                    i[5] = "south"

                elif i[5] == "south":
                    i[6] = "east"

                elif i[6] == "east":
                    i[4] = "north"

                elif i[4] == "north":
                    i[7] = "west"

                else:
                    None
   
            forward = "north"
            exit_helm = "south"
            right = "east"
            left = "west"

        elif left == "south":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                for j in range(3):
                    startX = i[0]
                    startZ = i[2]

                    i[0] = -(startZ - position.z) + position.x
                    i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[6] == "east":
                    i[4] = "north"

                elif i[4] == "north":
                    i[7] = "west"

                elif i[7] == "west":
                    i[5] = "south"

                elif i[5] == "south":
                    i[6] = "east"

                else:
                    None

            forward = "south"
            exit_helm = "north"
            right = "west"
            left = "east"

        elif left == "east":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                for j in range(3):
                    startX = i[0]
                    startZ = i[2]

                    i[0] = -(startZ - position.z) + position.x
                    i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[4] == "north":
                    i[7] = "west"

                elif i[7] == "west":
                    i[5] = "south"

                elif i[5] == "south":
                    i[6] = "east"

                elif i[6] == "east":
                    i[4] = "north"

                else:
                    None
               
            forward = "east"
            exit_helm = "west"
            right = "south"
            left = "north"

        elif left == "west":
            for i in shipBlocks:
                mc.setBlock(i[0], i[1], i[2], block.AIR.id)
          
            for i in shipBlocks:
                for j in range(3):
                    startX = i[0]
                    startZ = i[2]

                    i[0] = -(startZ - position.z) + position.x
                    i[2] = (startX - position.x) + position.z

                mc.setBlock(i[0], i[1], i[2], i[3])

                if i[5] == "south":
                    i[6] = "east"

                elif i[6] == "east":
                    i[4] = "north"

                elif i[4] == "north":
                    i[7] = "west"

                elif i[7] == "west":
                    i[5] = "south"

                else:
                    None
               
            forward = "west"
            exit_helm = "east"
            right = "north"
            left = "south"

    #move the ship up
    if direction == "up":
        for i in shipBlocks:
            i[1] += 1
            mc.setBlock(i[0], i[1], i[2], i[3])

            if i[9] == "below":
                mc.setBlock(i[0], i[1] - 1, i[2], block.AIR.id)

        position.y += 1

    #move the ship down
    if direction == "down":
        for i in shipBlocks:
            i[1] -= 1
            mc.setBlock(i[0], i[1], i[2], i[3])

            if i[8] == "above":
                mc.setBlock(i[0], i[1] + 1, i[2], block.AIR.id)

        position.y -= 1
                           
    mc.player.setPos(position.x, position.y, position.z)
    position = mc.player.getPos()
