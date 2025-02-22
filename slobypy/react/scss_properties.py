POSSIBLE_ATTRIBUTES = ["_webkit_line_clamp", "name", "scss_group", "className", "_webkit_text_fill_color", "_webkit_text_stroke",
                       "_webkit_text_stroke_color", "_webkit_text_stroke_width", "accent_color", "align_content",
                       "align_items", "align_self", "align_tracks", "all", "animation", "animation_composition",
                       "animation_delay", "animation_direction", "animation_duration", "animation_fill_mode",
                       "animation_iteration_count", "animation_name", "animation_play_state", "animation_timeline",
                       "animation_timing_function", "appearance", "aspect_ratio", "backdrop_filter",
                       "backface_visibility", "background", "background_attachment", "background_blend_mode",
                       "background_clip", "background_color", "background_image", "background_origin",
                       "background_position", "background_position_x", "background_position_y", "background_repeat",
                       "background_size", "block_size", "border", "border_block", "border_block_color",
                       "border_block_end", "border_block_end_color", "border_block_end_style",
                       "border_block_end_width", "border_block_start", "border_block_start_color",
                       "border_block_start_style", "border_block_start_width", "border_block_style",
                       "border_block_width", "border_bottom", "border_bottom_color", "border_bottom_left_radius",
                       "border_bottom_right_radius", "border_bottom_style", "border_bottom_width",
                       "border_collapse", "border_color", "border_end_end_radius", "border_end_start_radius",
                       "border_image", "border_image_outset", "border_image_repeat", "border_image_slice",
                       "border_image_source", "border_image_width", "border_inline", "border_inline_color",
                       "border_inline_end", "border_inline_end_color", "border_inline_end_style",
                       "border_inline_end_width", "border_inline_start", "border_inline_start_color",
                       "border_inline_start_style", "border_inline_start_width", "border_inline_style",
                       "border_inline_width", "border_left", "border_left_color", "border_left_style",
                       "border_left_width", "border_radius", "border_right", "border_right_color",
                       "border_right_style", "border_right_width", "border_spacing", "border_start_end_radius",
                       "border_start_start_radius", "border_style", "border_top", "border_top_color",
                       "border_top_left_radius", "border_top_right_radius", "border_top_style", "border_top_width",
                       "border_width", "bottom", "box_decoration_break", "box_shadow", "box_sizing", "break_after",
                       "break_before", "break_inside", "caption_side", "caret_color", "clear", "clip_path", "color",
                       "color_scheme", "column_count", "column_fill", "column_gap", "column_rule",
                       "column_rule_color", "column_rule_style", "column_rule_width", "column_span", "column_width",
                       "columns", "contain", "contain_intrinsic_block_size", "contain_intrinsic_height",
                       "contain_intrinsic_inline_size", "contain_intrinsic_size", "contain_intrinsic_width",
                       "content", "content_visibility", "counter_increment", "counter_reset", "counter_set",
                       "cursor", "direction", "display", "empty_cells", "filter", "flex", "flex_basis",
                       "flex_direction", "flex_flow", "flex_grow", "flex_shrink", "flex_wrap", "float", "font",
                       "font_family", "font_feature_settings", "font_kerning", "font_language_override",
                       "font_optical_sizing", "font_size", "font_size_adjust", "font_stretch", "font_style",
                       "font_synthesis", "font_variant", "font_variant_alternates", "font_variant_caps",
                       "font_variant_east_asian", "font_variant_ligatures", "font_variant_numeric",
                       "font_variant_position", "font_variation_settings", "font_weight", "forced_color_adjust",
                       "gap", "grid", "grid_area", "grid_auto_columns", "grid_auto_flow", "grid_auto_rows",
                       "grid_column", "grid_column_end", "grid_column_start", "grid_row", "grid_row_end",
                       "grid_row_start", "grid_template", "grid_template_areas", "grid_template_columns",
                       "grid_template_rows", "hanging_punctuation", "height", "hyphenate_character", "hyphens",
                       "image_orientation", "image_rendering", "image_resolution", "initial_letter",
                       "initial_letter_align", "inline_size", "inset", "inset_block", "inset_block_end",
                       "inset_block_start", "inset_inline", "inset_inline_end", "inset_inline_start", "isolation",
                       "justify_content", "justify_items", "justify_self", "justify_tracks", "left",
                       "letter_spacing", "line_break", "line_height", "line_height_step", "list_style",
                       "list_style_image", "list_style_position", "list_style_type", "margin", "margin_block",
                       "margin_block_end", "margin_block_start", "margin_bottom", "margin_inline",
                       "margin_inline_end", "margin_inline_start", "margin_left", "margin_right", "margin_top",
                       "margin_trim", "mask", "mask_border", "mask_border_mode", "mask_border_outset",
                       "mask_border_repeat", "mask_border_slice", "mask_border_source", "mask_border_width",
                       "mask_clip", "mask_composite", "mask_image", "mask_mode", "mask_origin", "mask_position",
                       "mask_repeat", "mask_size", "mask_type", "masonry_auto_flow", "math_depth", "math_shift",
                       "math_style", "max_block_size", "max_height", "max_inline_size", "max_width",
                       "min_block_size", "min_height", "min_inline_size", "min_width", "mix_blend_mode",
                       "object_fit", "object_position", "offset", "offset_anchor", "offset_distance", "offset_path",
                       "offset_position", "offset_rotate", "opacity", "order", "orphans", "outline",
                       "outline_color", "outline_offset", "outline_style", "outline_width", "overflow",
                       "overflow_anchor", "overflow_block", "overflow_clip_margin", "overflow_inline",
                       "overflow_wrap", "overflow_x", "overflow_y", "overscroll_behavior",
                       "overscroll_behavior_block", "overscroll_behavior_inline", "overscroll_behavior_x",
                       "overscroll_behavior_y", "padding", "padding_block", "padding_block_end",
                       "padding_block_start", "padding_bottom", "padding_inline", "padding_inline_end",
                       "padding_inline_start", "padding_left", "padding_right", "padding_top", "page_break_after",
                       "page_break_before", "page_break_inside", "paint_order", "perspective", "perspective_origin",
                       "place_content", "place_items", "place_self", "pointer_events", "position",
                       "print_color_adjust", "quotes", "resize", "right", "rotate", "row_gap", "ruby_align",
                       "ruby_position", "scale", "scroll_behavior", "scroll_margin", "scroll_margin_block",
                       "scroll_margin_block_end", "scroll_margin_block_start", "scroll_margin_bottom",
                       "scroll_margin_inline", "scroll_margin_inline_end", "scroll_margin_inline_start",
                       "scroll_margin_left", "scroll_margin_right", "scroll_margin_top", "scroll_padding",
                       "scroll_padding_block", "scroll_padding_block_end", "scroll_padding_block_start",
                       "scroll_padding_bottom", "scroll_padding_inline", "scroll_padding_inline_end",
                       "scroll_padding_inline_start", "scroll_padding_left", "scroll_padding_right",
                       "scroll_padding_top", "scroll_snap_align", "scroll_snap_stop", "scroll_snap_type",
                       "scroll_timeline", "scroll_timeline_axis", "scroll_timeline_name", "scrollbar_color",
                       "scrollbar_gutter", "scrollbar_width", "shape_image_threshold", "shape_margin",
                       "shape_outside", "tab_size", "table_layout", "text_align", "text_align_last",
                       "text_combine_upright", "text_decoration", "text_decoration_color", "text_decoration_line",
                       "text_decoration_skip", "text_decoration_skip_ink", "text_decoration_style",
                       "text_decoration_thickness", "text_emphasis", "text_emphasis_color",
                       "text_emphasis_position", "text_emphasis_style", "text_indent", "text_justify",
                       "text_orientation", "text_overflow", "text_rendering", "text_shadow", "text_size_adjust",
                       "text_transform", "text_underline_offset", "text_underline_position", "top", "touch_action",
                       "transform", "transform_box", "transform_origin", "transform_style", "transition",
                       "transition_delay", "transition_duration", "transition_property",
                       "transition_timing_function", "translate", "unicode_bidi", "user_select", "vertical_align",
                       "visibility", "white_space", "widows", "width", "will_change", "word_break", "word_spacing",
                       "writing_mode", "z_index"]
