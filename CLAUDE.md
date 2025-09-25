# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Coding Interview University** - a comprehensive study plan for technical interview preparation. This is a documentation-only repository containing study materials, not a software project with build/test commands.

## Repository Structure

### Core Content
- `README.md` - Main study plan with comprehensive curriculum (47K+ lines)
- `programming-language-resources.md` - Language-specific learning resources
- `translations/` - International translations of the main README
- `extras/cheat sheets/` - Reference materials (PDF cheat sheets for various topics)

### Key Areas of Focus
The repository covers computer science fundamentals for technical interviews:
- **Data Structures**: Arrays, linked lists, stacks, queues, hash tables, trees, graphs
- **Algorithms**: Sorting, searching, dynamic programming, recursion
- **System Design**: Scalability, data handling (for experienced developers)
- **Programming Languages**: C/C++, Python, Java, Go, JavaScript, HTML/CSS, Rust, Ruby
- **Additional Topics**: Big-O analysis, bit manipulation, design patterns, testing

### Content Organization
- **Main curriculum** in README.md with detailed study plan and resource links
- **Language-specific resources** separated into dedicated file
- **Translations** maintained in separate directory for international accessibility
- **Cheat sheets** in PDF format for quick reference during study

## Working with This Repository

### Content Updates
- All content is in Markdown format
- Main README.md is the primary document (extremely large file - 47K+ lines)
- Use section-based editing when modifying the main README
- Maintain consistency with existing formatting and link structure

### Translation Workflow
- Translations are in `translations/` directory
- Each language has its own README-{lang}.md file
- Translation status tracked in main README
- `translations/how-to.md` contains translation guidelines

### Quality Assurance
- GitHub workflow checks links monthly (`links_checker.yml`)
- Automated issue creation for broken links
- Link checker runs against main README.md only (excludes translations)

### Maintenance Tasks
- Link validation and updating
- Content accuracy verification
- New resource addition
- Translation coordination
- Cheat sheet updates

## Repository Characteristics
- **Type**: Educational content repository, not a code project
- **Primary Language**: Markdown documentation
- **Build System**: None (static content)
- **Testing**: Automated link checking only
- **Dependencies**: None
- **Deployment**: Static GitHub Pages hosting

## Python Learning Environment

### Directory Structure
- `python-practice/` - Python 實作練習目錄
  - `data-structures/` - 數據結構實作（陣列、鏈表、堆疊等）
  - `algorithms/` - 演算法實作（排序、搜尋、動態規劃等）
  - `tests/` - 測試檔案
  - `utils/` - 輔助工具和效能測試
  - `coding-interview-env/` - Python 虛擬環境

### Development Setup
```bash
# 切換到練習分支
git checkout python-learning

# 啟動虛擬環境
cd python-practice
source coding-interview-env/bin/activate

# 安裝依賴套件
pip install -r requirements.txt

# 運行測試
pytest

# 程式碼格式化
black .
```

### Learning Workflow
1. **Fork and Clone**: 已設置 upstream 為原始專案
2. **Branch Management**: 使用 `python-learning` 分支追蹤學習進度
3. **Implementation**: 在對應目錄實作數據結構和演算法
4. **Testing**: 使用 pytest 進行測試驗證
5. **Progress Tracking**: 在 README.md 中標記完成項目 [x]

### Code Quality Tools
- **pytest**: 測試框架
- **black**: 程式碼格式化
- **flake8**: 程式碼檢查
- **mypy**: 型別檢查
- **pytest-cov**: 測試覆蓋率

## Common Operations
- **Content editing**: Direct markdown editing of README files
- **Link validation**: Automated via GitHub Actions workflow
- **Translation updates**: Manual coordination with community contributors
- **Resource addition**: Update appropriate sections in main README or language resources file
- **Python Practice**: Use `python-practice/` directory for hands-on implementation
- **Progress Sync**: Regular `git pull upstream main` to stay updated with original project