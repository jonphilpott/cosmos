(* ::Package:: *)

CosmosImage[] := Import["/run/shm/cosmos.png"];


StarLocations[Img_, E_, C_] := 
	#[[2]][[1]] &/@
	ComponentMeasurements[EdgeDetect[Img],
	{"Centroid", "Eccentricity", "Circularity"}, #2 <E && #3 < C&];
StarLocations[Img_] := StarLocations[Img, 0.8, 1.7];


HighlightStars[Img_, E_, C_] := Show[Img, Graphics[{Red, Thick, Circle[#, 8]} &/@ StarLocations[Img, E, C]]];
HighlightStars[Img_] := HighlightStars[Img, 0.8, 1.7];

