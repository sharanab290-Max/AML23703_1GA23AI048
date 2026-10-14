rows, all_counts = [], {}
for bits in ENCODING:
    counts = send(superdense(bits))
    all_counts[bits] = counts
    rows.append({
        "Message": bits,
        "Alice's gates": " then ".join(g.upper() for g in ENCODING[bits]) or "I",
        "Bell state": which_bell(bits),
        "Decoded": max(counts, key=counts.get),
        "Counts": counts,
        "Success (%)": 100 * counts.get(bits, 0) / SHOTS,
    })
ex2 = pd.DataFrame(rows)
display(ex2)
print("All messages decoded correctly:", all(ex2["Message"] == ex2["Decoded"]))
 
display(superdense("11").draw("mpl", fold=-1))
display(plot_histogram([all_counts[b] for b in ENCODING],
                        legend=[f"sent {b}" for b in ENCODING],
                        title="Exercise 2 - Bob's results for each message"))

