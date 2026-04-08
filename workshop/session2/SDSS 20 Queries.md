# SDSS SkyServer Queries

These 20 queries are parsed from the Appendix of the technical report "Data Mining the SDSS SkyServer Database".

- Q1: Find all galaxies without saturated pixels within 1' of a given point.
- Q2: Find all galaxies with blue surface brightness between 23 and 25 magnitude per square arcseconds, and super galactic latitude (sgb) between (-10º, 10º), and declination less than zero.
- Q3: Find all galaxies brighter than magnitude 22, where the local extinction is >0.175.
- Q4: Find galaxies with an isophotal surface brightness (SB) larger than 24 in the red band, with an ellipticity >0.5, and with the major axis of the ellipse between 30" and 60" arc seconds (a large galaxy).
- Q5: Find all galaxies with a deVaucouleurs profile (r¼ falloff of intensity on disk) and the photometric colors consistent with an elliptical galaxy.
- Q6: Find galaxies that are blended with a star and output the deblended galaxy magnitudes.
- Q7: Provide a list of star-like objects that are 1% rare.
- Q8: Find all objects with unclassified spectra.
- Q9: Find quasars with a line width >2000 km/s and 2.5 < redshift < 2.7.
- Q10: Find galaxies with spectra that have an equivalent width in Ha >40Å.
- Q11: Find all elliptical galaxies with spectra that have an anomalous emission line.
- Q12: Create a gridded count of galaxies with u-g > 1 and r < 21.5 over -5 < declination < 5, and 175 < right ascension < 185, on a grid of 2' arc minutes.
- Q13: Create a count of galaxies for each of the HTM triangles which satisfy a certain color cut, like 0.7u-0.5g-0.2i < 1.25 and r < 21.75, output it in a form adequate for visualization.
- Q14: Find stars with multiple measurements that have magnitude variations >0.1.
- Q15: Provide a list of moving objects consistent with an asteroid.
- Q16: Find all objects similar to the colors of a quasar at 5.5 < redshift < 6.5.
- Q17: Find binary stars where at least one of them has the colors of a white dwarf.
- Q18: Find all objects within 30 arcseconds of one another that have very similar colors: that is where the color ratios u-g, g-r, r-i are less than 0.05m.
- Q19: Find quasars with a broad absorption line in their spectra and at least one galaxy within 10 arcseconds.
- Q20: For each galaxy in the LRG data set (Luminous Red Galaxy), in 160 < right ascension < 170, count of galaxies within 30" of it that have a photoZ within 0.05 of that galaxy.
