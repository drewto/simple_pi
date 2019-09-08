import time

def calculate_pi():
	pi_over_four = 0
	i = 1
	pos_or_neg = 1
	dif = 1

	while True:

		pi_over_four += dif
		i += 2
		pos_or_neg *= -1
		dif = (1 / i) * pos_or_neg
		pi = 4 * pi_over_four
		print("Pi: {}".format(pi))

if __name__ == "__main__":
	calculate_pi()