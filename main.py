# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


# part 1


def greet(name, greeting_template="Hello, <name>!"):
    template_split = greeting_template.split("<name>")
    before_split = template_split[0]
    after_split = template_split[1]
    greeting_template = before_split + name + after_split

    return greeting_template


# part 2


def force(mass, body="earth"):
    bodies = {
        "mercury": 3.7,
        "venus": 8.9,
        "earth": 9.8,
        "moon": 1.6,
        "mars": 3.7,
        "jupiter": 23.1,
        "saturn": 9.0,
        "uranus": 8.7,
        "neptune": 11.0,
        "pluto": 0.7,
    }

    return mass * bodies[body]


# part 3


def pull(m1, m2, d):
    return 6.674 * 10**-11 * ((m1 * m2) / d**2)
