theta = 0
stars = []
falling_structures = []


def setup():
    size(800, 800, P3D)
    smooth(100)
    
    global obj_model
    obj_model = loadShape("penguin1.obj")

    # Create initial falling structures
    for _ in range(300):
        x = random(-width / 2, width / 2)
        y = random(-height / 2, height / 2)
        z = random(-500, 500)
        size = random(20, 50)
        falling_structures.append({"position": PVector(x, y, z), "size": size})


def draw():
    global theta
    background(0)
    stroke(0)
    translate(width / 2, height / 2, 0)
    

    scale(1)  # Adjust the scale based on your preference
    rotateX(theta)
    rotateY(theta)
    shape(obj_model)

    # Draw falling structures
    for structure in falling_structures:
        x, y, z = structure["position"].array()
        box_size = structure["size"]

        # Change color based on Y-axis position
        fill(50, map(y, -height / 2, height / 2, y, y), x)

        pushMatrix()
        translate(x, y, z)
        box(box_size)
        popMatrix()

        # Update position for the falling effect
        structure["position"].y += 5  # Adjust the falling speed based on your preference
        if structure["position"].y > height / 2:
            structure["position"].y = -height / 2

    theta += 0.0155

    rotateY(theta)

    sphere_size = 200 + 20 * sin(theta * 2)

    fill(int(sin(theta) * 500), 20, 320)
    sphereDetail(10)
    sphere(sphere_size)
