# Automotive SPICE PAM v4.0 ReqMd

This directory contains a ReqMd representation of the Automotive SPICE Process Assessment Model v4.0.

Source document:

- <https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf>

The content is organized as requirement-style Markdown sections so that ASPICE process outcomes, base practices, and work products can be traced through ReqMd indexes.

## Indexes

- [`@.md`](@.md): identifier index for process, practice, and work product requirement sections.
- [`=.md`](=.md): helper index for work product and supporting concept links.

## Documents

Process-area files such as `SYS_2_System_Requirements_Analysis.md`, `SWE_1_Software_Requirements_Analysis.md`, and `SUP_8_Configuration_Management.md` contain the ReqMd sections derived from the PAM process content.

`WP_Information_Items.md` contains work product information item sections.

When editing these files, update the derived indexes with:

```powershell
python ..\.codex\skills\reqmd\scripts\update_index.py .
python ..\.codex\skills\reqmd\scripts\validate_reqmd.py .
```
