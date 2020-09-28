#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return 0

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	dot_product = v1[0] * v2[0] + v1[1] * v2[1]
	return dot_product == 0


def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).7
	sum =0
	num_value = 0
	#pour chaque element on utilise for in
	for v in values:
		if v >= 0:
			sum += v
			num_value += 1
	return sum/num_value


def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	bill_values = [20,10,5,1]
	result = [0,0,0,0]

	i = 0
	for bill in bill_values:
		if value >= bill:
			result[i] = value // bill
			value = value % bill
			i += 1


	return result
if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
