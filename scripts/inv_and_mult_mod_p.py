a = []
b = []
comp = []
bit = []

# p stores the working modulus
p = '06FE5D541F71C0E12909F97BADC668562B5045CB25748084E9867D6EBE876DA959B1A13F7CC76E3EC968549F878A8EEB'
p = int(p, 16)

i = 0
with open("scripts/abcomp_output") as file:
	for line in file:
		if (i == 0):
			line = line.strip("a: ")
			a.append(int(line,16))
		elif (i == 1):
			line = line.strip("b: ")
			b.append(int(line,16))
		elif (i == 2):
			line = line.strip("comp: ")
			comp.append(int(line,16))
		elif (i == 3):
			line = line.strip("bit: ")
			bit.append(int(line))
		i = (i + 1) % 4

for q in range(0, len(a)):
    #if (bit[q] == 1):
    #ainv = pow (a[q], p-2, p)
    #binv = pow (b[q], p-2, p)
    #acomp = (ainv * b[q]) % p
    bcomp = (b[q] * a[q]) % p
    print('a*b: {:x}'.format(bcomp))
    #print('binv*a: {:x}'.format(bcomp))
    print('original: {:x}'.format(comp[q] % p))
    print()
		#print(str(comp[q] == rcomp))
    #else:
    #    binv = pow(b[q], p-2, p)
    #    rcomp = (binv * a[q]) % p
    #    print('{:x}'.format(rcomp))
    #    print('{:x}'.format(comp[q]))
    #    print()
        #print(str(comp[q] == rcomp))


''' section of code to add to compress_psiS at the end (uncommented) for testing
	/* print a, b, and comp for testing purposes //
	from_Montgomery_mod_order(a, a, CurveIsogeny->Border, (digit_t*)&Montgomery_rprime);
	from_Montgomery_mod_order(b, b, CurveIsogeny->Border, (digit_t*)&Montgomery_rprime);

	printf("a: ");
	for (int i = 0; i < NWORDS_ORDER; i++) {
		printf("%0llX", a[i]);
	} printf("\n");

	printf("b: ");
	for (int i = 0; i < NWORDS_ORDER; i++) {
		printf("%0llX", b[i]);
	} printf("\n");

	printf("comp: ");
	for (int i = 0; i < NWORDS_ORDER; i++) {
		printf("%0llX", comp[i]);
	} printf("\n");

	printf("bit: ");
	for (int i = 0; i < NWORDS_ORDER; i++) {
		printf("%d", *compBit);
	} printf("\n");
	//-------------------------------------------*/
'''
