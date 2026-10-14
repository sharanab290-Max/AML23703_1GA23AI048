qc_01 = superdense("01")
print(qc_01.draw(output="text"))
 
pre_measure = Statevector(qc_01.remove_final_measurements(inplace=False))
print("Bob's register before measuring:",
      {str(k): round(float(v), 3) for k, v in pre_measure.probabilities_dict().items() if v > 1e-9})
 
counts_01 = send(qc_01)
print("Message sent     : 01")
print("Bob's counts      :", counts_01)
print("Decoded message   :", max(counts_01, key=counts_01.get))
print(f"Success rate      : {counts_01.get('01', 0) / SHOTS:.1%}")

