"""
For parsing description text into its component parts or vice versa.
Full of horrors stemming from using YouTube as a file store.
I accept full judgement for this terrifying and brittle parsing code.
"""
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class DescriptionParts:
    sponsored_links: Optional[str] = None
    donation_links: Optional[str] = None
    description: Optional[str] = None
    video_links: Optional[str] = None
    community_links: Optional[str] = None
    affiliate_links: Optional[str] = None
    music: Optional[str] = None
    chapters: Optional[str] = None


mcoding_title: str = "― mCoding with James Murphy (https://mcoding.io)"
description_title: str = "IN THIS VIDEO..."
community_title: str = "BE ACTIVE IN MY COMMUNITY 😄"
donation_title: str = "SUPPORT ME ⭐"
affiliate_title: str = "AFFILIATES AND REFERRALS"
music_title: str = "MUSIC"
chapters_title: str = "CHAPTERS"

current_community_links = """Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding"""

current_section_separator = "---------------------------------------------------"

current_affiliate_links = ""


def is_donation_section_text(s: str) -> bool:
    s = s.lower()
    return 'patreon' in s and 'paypal' in s


def is_sponsored_section_text(s: str) -> bool:
    s = s.lower()
    return bool(re.search(r'try\s+\w+:\s+http', s)) or ('thanks' in s and 'sponsoring' in s)


def description_to_parts(desc: str) -> DescriptionParts:
    sections = {}
    current_section = []
    current_section_title = ""
    lines = desc.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("-----------------"):
            assert i != 0
            next_section_title = current_section.pop()
            sections[current_section_title] = current_section
            current_section_title = next_section_title
            current_section = []
        else:
            current_section.append(line.strip())
    sections[current_section_title] = current_section

    parts = DescriptionParts()

    def combine_lines(ls):
        return '\n'.join(ls).strip()

    for title, section_lines in sections.items():
        if title == description_title:
            mcoding_title_idx = section_lines.index(mcoding_title)
            parts.description = combine_lines(section_lines[:mcoding_title_idx])
            parts.video_links = combine_lines(section_lines[mcoding_title_idx + 1:])
        elif title == music_title:
            parts.music = combine_lines(section_lines)
        elif title == community_title:
            parts.community_links = combine_lines(section_lines)
        elif title == donation_title:
            parts.donation_links = combine_lines(section_lines)
            assert is_donation_section_text(parts.donation_links)
        elif title == affiliate_title:
            parts.affiliate_links = combine_lines(section_lines)
        elif title == chapters_title:
            parts.chapters = combine_lines(section_lines)
        elif title == "":
            pass
        else:
            raise ValueError(f"Unexpected title {title}")

    # figure out what section without title is
    assert "" in sections, sections.keys()
    untitled_section = sections.pop("")
    section_text = combine_lines(untitled_section)
    if is_sponsored_section_text(section_text):
        parts.sponsored_links = section_text
    elif is_donation_section_text(section_text):
        parts.donation_links = section_text
    else:
        if parts.description is not None:
            raise ValueError(f"Description should be empty: {parts.description=}")
        parts.description = section_text

    return parts


def parts_to_description_v1(parts: DescriptionParts) -> str:
    desc = ""
    if parts.sponsored_links:
        desc += f'{parts.sponsored_links}\n'
    else:
        desc += f'{parts.donation_links}\n'

    assert parts.description
    desc += f'\n{description_title}\n{current_section_separator}\n{parts.description}\n\n{mcoding_title}\n'

    if parts.video_links:
        desc += f'\n{parts.video_links}\n'

    if parts.affiliate_links:
        desc += f'\n{affiliate_title}\n{current_section_separator}\n{parts.affiliate_links}\n'

    if parts.sponsored_links:
        desc += f'\n{donation_title}\n{current_section_separator}\n{parts.donation_links}\n'

    assert parts.community_links
    desc += f'\n{community_title}\n{current_section_separator}\n{parts.community_links}\n'

    if parts.music:
        desc += f'\n{music_title}\n{current_section_separator}\n{parts.music}\n'

    if parts.chapters:
        desc += f'\n{chapters_title}\n{current_section_separator}\n{parts.chapters}\n'

    return desc.strip()


def parts_to_description_v2(parts: DescriptionParts) -> str:
    desc = ""
    if parts.sponsored_links:
        desc += f'{parts.sponsored_links}\n'
        desc += f'\n{description_title}\n{current_section_separator}\n'

    assert parts.description
    desc += f'{parts.description}\n\n{mcoding_title}\n'

    if parts.video_links:
        desc += f'\n{parts.video_links}\n'

    if parts.affiliate_links:
        desc += f'\n{affiliate_title}\n{current_section_separator}\n{parts.affiliate_links}\n'

    if parts.donation_links:
        desc += f'\n{donation_title}\n{current_section_separator}\n{parts.donation_links}\n'

    if parts.community_links:
        desc += f'\n{community_title}\n{current_section_separator}\n{parts.community_links}\n'

    if parts.music:
        desc += f'\n{music_title}\n{current_section_separator}\n{parts.music}\n'

    if parts.chapters:
        desc += f'\n{chapters_title}\n{current_section_separator}\n{parts.chapters}\n'

    return desc.strip()
