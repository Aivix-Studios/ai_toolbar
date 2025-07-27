# AI Toolbar - Visual Design Overview

## Application Layout

The AI Toolbar application features a modern cyberpunk-themed interface with the following layout:

### Main Window (1200x800 pixels)
```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│ File   View   Tools   Help                                                  [_][□][X] │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ 🤖 CHATBOTS     ┃ 🔧 AGENTS       ┃ 💻 LOW-CODE TOOLS                               │
│ [ChatGPT]  [Gemini]  [Grok]  [Claude] ┃ [Manus]  [Mini-Max] ┃ [Copilot] [Windsurf] [AI Studio] │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  ┌─[Welcome]─┬─[ChatGPT - Chat Session]─┬─[Gemini - New Chat]─┐                    │
│  │                                                             │                    │
│  │                Welcome to AI Toolbar                       │                    │
│  │                                                             │                    │
│  │         Click any AI tool button above to start            │                    │
│  │                                                             │                    │
│  │         🔥 Available Tools:                                 │                    │
│  │         • ChatGPT, Gemini, Grok, Claude (Chatbots)         │                    │
│  │         • Manus, Mini-Max (AI Agents)                      │                    │
│  │         • GitHub Copilot, Windsurf, AI Studio (Dev Tools) │                    │
│  │                                                             │                    │
│  │         ⌨️ Hotkeys:                                          │                    │
│  │         • Alt + W: Show/Hide toolbar                       │                    │
│  │         • Click X on tabs to close them                    │                    │
│  │                                                             │                    │
│  └─────────────────────────────────────────────────────────────┘                    │
│                                                                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ AI Toolbar ready - Press Alt+W to toggle visibility                                │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Color Scheme (Cyberpunk Theme)

### Primary Colors
- **Background**: #0d1117 (Dark GitHub-style background)
- **Secondary Background**: #161b22 (Toolbar/menu background)
- **Borders**: #30363d (Subtle borders)
- **Text**: #c9d1d9 (Light gray text)

### Accent Colors by Category
- **Chatbots**: #58a6ff (Blue) - ChatGPT, Gemini, Grok, Claude
- **Agents**: #a5f3fc (Cyan) - Manus, Mini-Max  
- **Low-Code**: #7c3aed (Purple) - GitHub Copilot, Windsurf, AI Studio

### Interactive States
- **Hover**: Buttons glow with category color + shadow effect
- **Active**: Button filled with category color, white text
- **Selected Tab**: Tab highlighted with blue accent

## Key Visual Features

### 1. Toolbar Section
- Organized by categories with visual separators
- Category labels with color-coded badges
- Tool buttons with hover glow effects
- SVG icons for each AI tool

### 2. Tab Management
- Chrome-style tabs at bottom of web area
- Close buttons (X) on each tab
- Active tab highlighted
- Tab titles show tool name + page title

### 3. Web Content Area
- Full QWebEngine integration
- Each AI tool loads in its own tab
- Welcome screen when no tools open
- Maintains session state and cookies

### 4. System Integration
- **Minimized State**: Shows as single icon in system panel
- **Tray Icon**: Right-click menu with Show/Hide/Quit options
- **Global Hotkey**: Alt + W toggles visibility from anywhere
- **Always on Top**: Optional setting for staying above other windows

## Responsive Behavior

### Window States
1. **Normal**: Full application window with toolbar and tabs
2. **Hidden**: Window hidden, accessible via hotkey or tray
3. **Minimized**: Icon in system panel showing tab count
4. **Always on Top**: Stays above other applications when enabled

### Interaction Flow
1. User presses Alt + W or clicks system tray
2. Window appears with cyberpunk styling
3. User clicks AI tool button (e.g., ChatGPT)
4. New tab opens with tool's website
5. User can switch between tabs or open more tools
6. Alt + W hides window but keeps tabs active
7. Returning shows same tabs and sessions

## Accessibility Features
- High contrast cyberpunk colors
- Clear visual hierarchy
- Tooltips on all buttons
- Keyboard navigation support
- Consistent interaction patterns