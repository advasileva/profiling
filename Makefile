NUM_CASES = 3

init:
	pip install snakeviz

profile:
	bash ./scripts/profile.sh ${NUM_CASES}

viz:
	bash ./scripts/viz.sh ${NUM_CASES}
