# LamenessDetectionPlayground

A curated playground of open-source projects for video-based animal behaviour analysis and dairy-cow lameness detection. This repository aggregates code and docs from several interesting reference implementations so they can be compared, learned from, and extended side-by-side. Contributions that add more relevant projects are warmly welcome.

Note: Each subfolder preserves the original project’s structure and license. Please read and follow the upstream licenses when using any code.

## What’s Inside

- **00 - Russello (2024): Video‑based Lameness Detection**
  <p align="center">
    <img src="00-Cow_VBLD_2024/pic/0.jpg"  width="50%">
  </p>

  - Paper: [Video-based automatic lameness detection of dairy cows using pose estimation and multiple locomotion traits - Russello et al. (2024)](https://www.sciencedirect.com/science/article/pii/S0168169924004319)  
  - Source Code: [github](https://github.com/hrussel/lameness-detection)
  
- **01 - Price (2025): Animal Behaviour Inference Framework (Smarter‑Labelme + Behaviour Workflow)**
  <p align="center">
    <img src="01-ABIF_2025/pic/0.png"  width="90%">
  </p>

  - Paper: [A framework for fast, large-scale, semi-automatic inference of animal behaviour from monocular videos - Price et al. (2025)](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.70124)  
  - Source Code: [github](https://github.com/robot-perception-group/Animal-Behaviour-Inference-Framework) / [zenodo](https://zenodo.org/records/15834944)
  - Datasets: [darus](https://darus.uni-stuttgart.de/dataset.xhtml?persistentId=doi:10.18419/DARUS-5162) / [keeper](https://keeper.mpdl.mpg.de/d/a9822e000aff4b5391e1/)

- **02 - Elhorst (2025): Browser‑Based Behaviour Coding**
  <p align="center">
    <img src="02-behave_2025/pic/0.png"  width="90%">
  </p>

  - Paper: [A framework for fast, large-scale, semi-automatic inference of animal behaviour from monocular videos - Elhorst et al. (2025)](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.70124)  
  - Source Code: [github](https://github.com/behave-app/behave) 
  - Website application address: [behave.claude-apps.com](https://behave.claude-apps.com/)
- **03-Kamikouchi (2023): End‑to‑End YOLO/GUI Pipeline”**

  <p align="center">
    <img src="03-YORU_2023/docs/imgs/title_movie.gif" width="50%">
  </p>

  - Paper: [YORU: social behavior detection based on user-defined animal appearance using deep learning - Kamikouchi et al. (2024)](https://www.biorxiv.org/content/10.1101/2024.11.12.623320v1.full)  
  - Source Code: [github](https://github.com/Kamikouchi-lab/YORU)

- **04- TBA** (Feel free to add any other fun and relevant projects or references here!)


**Russello (2024): Video‑based Lameness Detection**
- Focus: Pose estimation + multiple locomotion traits to automatically detect lameness in dairy cows.
- How it works: Extracts gait keypoints from video, computes locomotion features, and trains classical ML models for lameness classification.
- Try it: Set up the conda env and run training.
  - Env: `00-Cow_lameness_detection_using_pose_estimation_and_multiple_locomotion_traits_2024/environment-short.yml`
  - Entry: `00-Cow_lameness_detection_using_pose_estimation_and_multiple_locomotion_traits_2024/train_ml.py`
- More: See `00-Cow_lameness_detection_using_pose_estimation_and_multiple_locomotion_traits_2024/README.md` (includes citation to Computers and Electronics in Agriculture, 2024).

**Price (2025): Animal Behaviour Inference Framework**
- Focus: A practical workflow built around Smarter‑Labelme to annotate, train animal detectors, and classify behaviours.
- How it works: Three streams — S1 annotate/train detector, S2 label behaviours leveraging the detector, S3 semi‑automate behaviour annotation for rapid iteration.
- Try it: Install Smarter‑Labelme and follow the “howto” workflow.
  - Guide: `01-Animal-Behaviour-Inference-Framework_2025/howto/README.md`
  - Tools: `smarter_labelme` CLI for video→frames, annotation, tracking, dataset prep, and training.

**BEHAVE (2025): Browser‑Based Behaviour Coding**
- Focus: Zero‑install, in‑browser tool to code behaviour from long videos, using AI to skip background‑only sections.
- Highlights: Open‑source (MIT), runs locally in the browser, anonymous usage stats only, programmable ethogram, timestamp/frame extraction, verification viewer.
- Learn more: `02-behave_2025/static/index.md` (includes quick start and app links in the original site structure).

**YORU (2023): End‑to‑End YOLO/GUI Pipeline**

<p align="center">
  <img src="03-YORU_2023/logos/YORU_logo.png" width="40%">
</p>

- Focus: A GUI suite for dataset creation, training, evaluation, offline analysis, and real‑time/closed‑loop processing.
- How it works: Project‑oriented pipeline with frame capture, labeling GUIs, training utilities, and real‑time inference.
- Try it: Requires Chrome, Conda, and PyTorch; run the module entry point.
  - Env file: `03-YORU_2023/YORU.yml`
  - Docs: `03-YORU_2023/docs/`
  - Run: `python -m yoru` from the `03-YORU_2023` project folder (after environment setup).

## Suggested Use

- Compare approaches: Review how pose/traits (Russello), annotation+workflow (Price), browser‑first coding (BEHAVE), and GUI/YOLO pipelines (YORU) tackle related problems.
- Reuse components: Borrow data handling, labeling flows, or training scripts as references when building your own pipeline.
- Prototype ideas: Start from the project that best matches your constraints (browser‑based, GUI, or script‑first) and iterate.

## Contributing

- Add references: PRs adding other relevant projects, datasets, or tutorials are welcome.
- Keep it tidy: Include a short description, upstream link, license, and a minimal “try it” note for each addition.
- Be respectful: Do not remove or alter upstream licenses; link to the original authors and papers when available.

## Attribution & Licenses

- All subprojects are credited to their original authors and keep their original licenses within their folders.
- If you use a specific subproject, please cite and follow its license and citation instructions.

## System Notes

- GPU recommended: Training and inference workflows in several subprojects benefit from NVIDIA GPUs and CUDA.
- Large data: Example datasets or media may be partial; follow each subproject’s README for data expectations.
