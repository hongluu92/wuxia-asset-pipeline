# Wuxia Asset Pipeline

Pipeline sản xuất asset nhân vật võ hiệp 2.5D đầu tiên (`wudang_male_01`) cho PC + Mobile.

**Thiết bị:** Mac M4 16GB. **Công cụ:** Gemini (concept, texture), Blender (rig/animation/render), Mixamo (animation), Unity 6 URP (game), Python (packing/validation).

## Mục tiêu MVP

- Nhân vật kiếm khách Võ Đang (từ free base asset có license phù hợp)
- 3 animation: `Idle`, `Walk`, `Attack`
- 8 hướng: `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, `NW`
- PNG RGBA có pivot đồng nhất, sprite atlas + JSON
- Demo import và playback được trong Unity

## Cấu trúc

- `ArtPipeline/concepts`: reference từ Gemini, ghi rõ provenance.
- `ArtPipeline/free_assets`: asset nguồn có license; không commit file lớn/bản quyền không cho phép.
- `ArtPipeline/licenses`: lưu URL, tác giả, license và thời điểm tải.
- `ArtPipeline/blender`: scene `.blend`, camera, rig.
- `ArtPipeline/animations`: clips đầu vào.
- `ArtPipeline/renders`: PNG từng frame (generated, ignored).
- `ArtPipeline/atlases`: atlas build (generated, ignored).
- `ArtPipeline/metadata`: metadata mô tả animation, pivot, events.
- `ArtPipeline/scripts`: công cụ Python hỗ trợ packing và validation.
- `UnityProject`: thư mục Unity skeleton, tạo project Unity 6 URP tại đây bằng Unity Hub trước khi dùng.

## Bắt đầu

1. Tạo concept sheet bằng Gemini theo `docs/character_brief.md`.
2. Tải base model free + lưu thông tin tại `ArtPipeline/licenses/asset_manifest.csv`.
3. Thiết lập nhân vật và 3 Action trong Blender, khóa camera orthographic.
4. Render PNG RGBA và kiểm tra pivot.
5. Dùng `python3 ArtPipeline/scripts/pack_grid.py --input ... --output ...` để tạo atlas PNG + JSON.
6. Mở Unity 6 URP và import ảnh/metadata, kiểm thử trên Mac/Android.

**Lưu ý:** Mẫu repo chứa scaffolding và tool tối giản; chưa có nhân vật, scene Unity hay workflow AI hoàn chỉnh.
