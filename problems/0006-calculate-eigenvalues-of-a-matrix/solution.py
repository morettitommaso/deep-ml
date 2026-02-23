def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import cmath

	a, b = matrix[0]
	c, d = matrix[1]

	trace = a + d
	determinant = (a*d)-(b*c)

	discriminant = trace**2 - 4 * determinant

	sqrt_discriminant = cmath.sqrt(discriminant)

	lambda1 = (trace + sqrt_discriminant) / 2
	lambda2 = (trace - sqrt_discriminant) / 2

	eigenvalues = [lambda1, lambda2]
	eigenvalues.sort(key=lambda x: x.real, reverse=True)

	result = []
	for val in eigenvalues:
		if abs(val.imag) < 1e-12:
			result.append(float(val.real))
		else:
			result.append(val)

	return result

